# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genom.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='genom.proto',
  package='GenomEvaluation',
  syntax='proto3',
  serialized_pb=_b('\n\x0bgenom.proto\x12\x0fGenomEvaluation\"\x19\n\x05Genom\x12\x10\n\x04gene\x18\x01 \x03(\x02\x42\x02\x10\x01\"G\n\nIndividual\x12%\n\x05genom\x18\x01 \x01(\x0b\x32\x16.GenomEvaluation.Genom\x12\x12\n\nevaluation\x18\x02 \x01(\x02\">\n\nGeneration\x12\x30\n\x0bindividuals\x18\x01 \x03(\x0b\x32\x1b.GenomEvaluation.Individual\"\x07\n\x05\x45mpty2\x99\x01\n\x0fGenomEvaluation\x12\x46\n\rGetIndividual\x12\x16.GenomEvaluation.Genom\x1a\x1b.GenomEvaluation.Individual\"\x00\x12>\n\nStopServer\x12\x16.GenomEvaluation.Empty\x1a\x16.GenomEvaluation.Empty\"\x00\x62\x06proto3')
)




_GENOM = _descriptor.Descriptor(
  name='Genom',
  full_name='GenomEvaluation.Genom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gene', full_name='GenomEvaluation.Genom.gene', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=57,
)


_INDIVIDUAL = _descriptor.Descriptor(
  name='Individual',
  full_name='GenomEvaluation.Individual',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='genom', full_name='GenomEvaluation.Individual.genom', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evaluation', full_name='GenomEvaluation.Individual.evaluation', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=130,
)


_GENERATION = _descriptor.Descriptor(
  name='Generation',
  full_name='GenomEvaluation.Generation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='individuals', full_name='GenomEvaluation.Generation.individuals', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=194,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='GenomEvaluation.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=203,
)

_INDIVIDUAL.fields_by_name['genom'].message_type = _GENOM
_GENERATION.fields_by_name['individuals'].message_type = _INDIVIDUAL
DESCRIPTOR.message_types_by_name['Genom'] = _GENOM
DESCRIPTOR.message_types_by_name['Individual'] = _INDIVIDUAL
DESCRIPTOR.message_types_by_name['Generation'] = _GENERATION
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Genom = _reflection.GeneratedProtocolMessageType('Genom', (_message.Message,), dict(
  DESCRIPTOR = _GENOM,
  __module__ = 'genom_pb2'
  # @@protoc_insertion_point(class_scope:GenomEvaluation.Genom)
  ))
_sym_db.RegisterMessage(Genom)

Individual = _reflection.GeneratedProtocolMessageType('Individual', (_message.Message,), dict(
  DESCRIPTOR = _INDIVIDUAL,
  __module__ = 'genom_pb2'
  # @@protoc_insertion_point(class_scope:GenomEvaluation.Individual)
  ))
_sym_db.RegisterMessage(Individual)

Generation = _reflection.GeneratedProtocolMessageType('Generation', (_message.Message,), dict(
  DESCRIPTOR = _GENERATION,
  __module__ = 'genom_pb2'
  # @@protoc_insertion_point(class_scope:GenomEvaluation.Generation)
  ))
_sym_db.RegisterMessage(Generation)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'genom_pb2'
  # @@protoc_insertion_point(class_scope:GenomEvaluation.Empty)
  ))
_sym_db.RegisterMessage(Empty)


_GENOM.fields_by_name['gene'].has_options = True
_GENOM.fields_by_name['gene']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))

_GENOMEVALUATION = _descriptor.ServiceDescriptor(
  name='GenomEvaluation',
  full_name='GenomEvaluation.GenomEvaluation',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=206,
  serialized_end=359,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetIndividual',
    full_name='GenomEvaluation.GenomEvaluation.GetIndividual',
    index=0,
    containing_service=None,
    input_type=_GENOM,
    output_type=_INDIVIDUAL,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StopServer',
    full_name='GenomEvaluation.GenomEvaluation.StopServer',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_EMPTY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GENOMEVALUATION)

DESCRIPTOR.services_by_name['GenomEvaluation'] = _GENOMEVALUATION

# @@protoc_insertion_point(module_scope)
