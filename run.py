import sys
import subprocess
from fcntl import fcntl, F_SETFL, F_GETFL
import os

def non_blocking_read(output):
    fd = output.fileno()
    fl = fcntl(fd, F_GETFL)
    fcntl(fd, F_SETFL, fl | os.O_NONBLOCK)
    try:
        return output.read()
    except:
        return ""

def get_first_node(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        return line.split()[0]

def run(genom_name, model_name, quantize_layer):
    server = subprocess.Popen('python src/services/genom_evaluation_server.py {} {}'.format(model_name, quantize_layer),
                            shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        s_line = non_blocking_read(server.stdout)
        if s_line:
            sys.stdout.write(s_line.decode('utf-8'))
            if 'Server Ready' in s_line.decode('utf-8'):
                break
            if not s_line and server.poll() is not None:
                print('Server Error.')
                return
    hostname = os.uname()[1]
    client_node = get_first_node(os.environ['GA_HOSTFILE'])
    if hostname in client_node or client_node in hostname:
        print("{} is a client node.".format(hostname))
        client = subprocess.Popen('./bin/client {} {} {}'
                                  .format(genom_name, model_name, quantize_layer), shell=True,
                                  stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while True:
            s_line = non_blocking_read(server.stdout)
            c_line = non_blocking_read(client.stdout)
            if s_line:
                sys.stdout.write("{}: {}".format(hostname, s_line.decode('utf-8')))
            elif server.poll() is not None:
                print('Server Error.')
                return
            if c_line:
                sys.stdout.write("client: {}".format(c_line.decode('utf-8')))
            elif client.poll() is not None:
                break
    else:
        while True:
            s_line = non_blocking_read(server.stdout)
            if s_line:
                sys.stdout.write("{}: {}".format(hostname, s_line.decode('utf-8')))
            elif server.poll() is not None:
                print('Server Error.')
                return

    server.kill()

        
if __name__=='__main__':
    argv = sys.argv
    if len(argv) != 4:
        print('Usage: python ga_executor.py <genom name> <model name> <quantize_layer>')
        exit()
    run(argv[1], argv[2], argv[3])

