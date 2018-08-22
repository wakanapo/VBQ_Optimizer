import copy
from concurrent import futures
import time
import os
pwd = os.getcwd()
import sys
sys.path.append(pwd+'/src/protos')
import genom_pb2
import genom_pb2_grpc
import grpc
from keras.applications.vgg16 import VGG16, preprocess_input
from keras import backend as K
from keras import optimizers
import numpy as np
import tensorflow as tf

import cifar10
import imagenet

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
val_X = []
val_y = []
g_W = []

def converter(partition):
    def f(arr):
        arr = np.asarray(arr)
        end_idx = len(partition) - 1
        for i in range(end_idx):
            arr[(arr > partition[i]) & (arr <= partition[i+1])] = (partition[i] + partition[i + 1]) /  2
        arr[arr <= partition[0]] = partition[0]
        arr[arr > partition[end_idx]] = partition[end_idx]
        return arr
    return f

def data_selector(model_name):
    if model_name == 'vgg_like' or model_name == 'hinton':
        _, _, val_X, val_y = cifar10.read_data()
    else:
        val_X, val_y = imagenet.load()
    return val_X, val_y

def model_selector(model_name, weights=True):
    if model_name == 'vgg_like' or model_name == 'hinton':
        if model_name == 'vgg_like':
            model_class = cifar10.Vgg_like();
            print("Model: vgg_like")
        else:
            model_class = cifar10.Hinton();
            print("Model: hinton")
        model = model_class.build((32, 32, 3))
        if weights:
            model.load_weights('data/'+model_class.name+'.h5')
            print("load weights: success.")
    else:
        print("Model: vgg16")
        if weights:
            model = VGG16(weights='data/vgg16.h5')
            print("load weights: success.")
        else:
            model = VGG16(weights=None)
    return model

def calculate_fitness(genom, model_name):
    with K.get_session().graph.as_default():
        print("start evaluation!")
        model = model_selector(model_name, weights=False)
        W_q = list(map(converter(genom.gene), copy.deepcopy(g_W)))
        print("quantize: success.")
        model.set_weights(W_q)
        model.compile(optimizer=optimizers.Adam(),
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])
        score = model.evaluate(val_X, val_y, verbose=0)
    K.clear_session()
    return score[1]

class GenomEvaluationServicer(genom_pb2_grpc.GenomEvaluationServicer):
    def __init__(self, genom_name):
        self.genom_name_ = genom_name
        
    def GetIndividual(self, request, context):
        return genom_pb2.Individual(genom=request,
                                    evaluation=calculate_fitness(request,
                                                                 self.genom_name_))

def serve(model_name):
    global val_X, val_y, g_W
    val_X, val_y = data_selector(model_name)
    val_X = preprocess_input(val_X)
    print("data load: success.")
    model = model_selector(model_name, weights=True)
    g_W = model.get_weights()
    print("model load: success.")
    print("Server Ready")
    sys.stdout.flush()
    server = grpc.server(futures.ThreadPoolExecutor())
    genom_pb2_grpc.add_GenomEvaluationServicer_to_server(
        GenomEvaluationServicer(model_name), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__=='__main__':
    argv = sys.argv
    if len(argv) < 2:
        print("Please set model name.")
        exit()
    serve(argv[1])

