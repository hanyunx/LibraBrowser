# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/cluster.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/cluster.proto',
  package='cluster',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x13proto/cluster.proto\x12\x07\x63luster\"#\n!SetRootChainConfirmedBlockRequest\"\x1b\n\x19\x46inalizeMinorBlockRequest\"3\n\x12\x43lusterSlaveStatus\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"5\n\x10MinorBlockHeader\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x15\n\rfull_shard_id\x18\x02 \x01(\r\"z\n\x13\x41\x64\x64RootBlockRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x0f\n\x07prev_id\x18\x02 \x01(\x0c\x12\x0e\n\x06height\x18\x03 \x01(\x04\x12\x36\n\x13minor_block_headers\x18\x04 \x03(\x0b\x32\x19.cluster.MinorBlockHeader\"p\n\x1a\x41\x64\x64MinorBlockHeaderRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\r\n\x05round\x18\x02 \x01(\x04\x12\x1b\n\x13prev_minor_block_id\x18\x03 \x01(\x0c\x12\x1a\n\x12prev_root_block_id\x18\x04 \x01(\x0c\"J\n\x1b\x41\x64\x64MinorBlockHeaderResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.cluster.ClusterSlaveStatus\"Q\n\"SetRootChainConfirmedBlockResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.cluster.ClusterSlaveStatus\"\x1c\n\x1a\x46inalizeMinorBlockResponse\"C\n\x14\x41\x64\x64RootBlockResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.cluster.ClusterSlaveStatus\"\x1d\n\x1bGetUnconfirmedHeaderRequest\"N\n\x1cGetUnconfirmedHeaderResponse\x12.\n\x0bheader_list\x18\x01 \x03(\x0b\x32\x19.cluster.MinorBlockHeader2\x9e\x03\n\x0c\x43lusterSlave\x12w\n\x1aSetRootChainConfirmedBlock\x12*.cluster.SetRootChainConfirmedBlockRequest\x1a+.cluster.SetRootChainConfirmedBlockResponse\"\x00\x12_\n\x12\x46inalizeMinorBlock\x12\".cluster.FinalizeMinorBlockRequest\x1a#.cluster.FinalizeMinorBlockResponse\"\x00\x12M\n\x0c\x41\x64\x64RootBlock\x12\x1c.cluster.AddRootBlockRequest\x1a\x1d.cluster.AddRootBlockResponse\"\x00\x12\x65\n\x14GetUnconfirmedHeader\x12$.cluster.GetUnconfirmedHeaderRequest\x1a%.cluster.GetUnconfirmedHeaderResponse\"\x00\x32s\n\rClusterMaster\x12\x62\n\x13\x41\x64\x64MinorBlockHeader\x12#.cluster.AddMinorBlockHeaderRequest\x1a$.cluster.AddMinorBlockHeaderResponse\"\x00\x62\x06proto3'
)




_SETROOTCHAINCONFIRMEDBLOCKREQUEST = _descriptor.Descriptor(
  name='SetRootChainConfirmedBlockRequest',
  full_name='cluster.SetRootChainConfirmedBlockRequest',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=67,
)


_FINALIZEMINORBLOCKREQUEST = _descriptor.Descriptor(
  name='FinalizeMinorBlockRequest',
  full_name='cluster.FinalizeMinorBlockRequest',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=96,
)


_CLUSTERSLAVESTATUS = _descriptor.Descriptor(
  name='ClusterSlaveStatus',
  full_name='cluster.ClusterSlaveStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='cluster.ClusterSlaveStatus.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='cluster.ClusterSlaveStatus.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=149,
)


_MINORBLOCKHEADER = _descriptor.Descriptor(
  name='MinorBlockHeader',
  full_name='cluster.MinorBlockHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cluster.MinorBlockHeader.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_shard_id', full_name='cluster.MinorBlockHeader.full_shard_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=204,
)


_ADDROOTBLOCKREQUEST = _descriptor.Descriptor(
  name='AddRootBlockRequest',
  full_name='cluster.AddRootBlockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cluster.AddRootBlockRequest.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prev_id', full_name='cluster.AddRootBlockRequest.prev_id', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='cluster.AddRootBlockRequest.height', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minor_block_headers', full_name='cluster.AddRootBlockRequest.minor_block_headers', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=328,
)


_ADDMINORBLOCKHEADERREQUEST = _descriptor.Descriptor(
  name='AddMinorBlockHeaderRequest',
  full_name='cluster.AddMinorBlockHeaderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cluster.AddMinorBlockHeaderRequest.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='round', full_name='cluster.AddMinorBlockHeaderRequest.round', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prev_minor_block_id', full_name='cluster.AddMinorBlockHeaderRequest.prev_minor_block_id', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prev_root_block_id', full_name='cluster.AddMinorBlockHeaderRequest.prev_root_block_id', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=330,
  serialized_end=442,
)


_ADDMINORBLOCKHEADERRESPONSE = _descriptor.Descriptor(
  name='AddMinorBlockHeaderResponse',
  full_name='cluster.AddMinorBlockHeaderResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cluster.AddMinorBlockHeaderResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=444,
  serialized_end=518,
)


_SETROOTCHAINCONFIRMEDBLOCKRESPONSE = _descriptor.Descriptor(
  name='SetRootChainConfirmedBlockResponse',
  full_name='cluster.SetRootChainConfirmedBlockResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cluster.SetRootChainConfirmedBlockResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=520,
  serialized_end=601,
)


_FINALIZEMINORBLOCKRESPONSE = _descriptor.Descriptor(
  name='FinalizeMinorBlockResponse',
  full_name='cluster.FinalizeMinorBlockResponse',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=603,
  serialized_end=631,
)


_ADDROOTBLOCKRESPONSE = _descriptor.Descriptor(
  name='AddRootBlockResponse',
  full_name='cluster.AddRootBlockResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cluster.AddRootBlockResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=633,
  serialized_end=700,
)


_GETUNCONFIRMEDHEADERREQUEST = _descriptor.Descriptor(
  name='GetUnconfirmedHeaderRequest',
  full_name='cluster.GetUnconfirmedHeaderRequest',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=702,
  serialized_end=731,
)


_GETUNCONFIRMEDHEADERRESPONSE = _descriptor.Descriptor(
  name='GetUnconfirmedHeaderResponse',
  full_name='cluster.GetUnconfirmedHeaderResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header_list', full_name='cluster.GetUnconfirmedHeaderResponse.header_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=733,
  serialized_end=811,
)

_ADDROOTBLOCKREQUEST.fields_by_name['minor_block_headers'].message_type = _MINORBLOCKHEADER
_ADDMINORBLOCKHEADERRESPONSE.fields_by_name['status'].message_type = _CLUSTERSLAVESTATUS
_SETROOTCHAINCONFIRMEDBLOCKRESPONSE.fields_by_name['status'].message_type = _CLUSTERSLAVESTATUS
_ADDROOTBLOCKRESPONSE.fields_by_name['status'].message_type = _CLUSTERSLAVESTATUS
_GETUNCONFIRMEDHEADERRESPONSE.fields_by_name['header_list'].message_type = _MINORBLOCKHEADER
DESCRIPTOR.message_types_by_name['SetRootChainConfirmedBlockRequest'] = _SETROOTCHAINCONFIRMEDBLOCKREQUEST
DESCRIPTOR.message_types_by_name['FinalizeMinorBlockRequest'] = _FINALIZEMINORBLOCKREQUEST
DESCRIPTOR.message_types_by_name['ClusterSlaveStatus'] = _CLUSTERSLAVESTATUS
DESCRIPTOR.message_types_by_name['MinorBlockHeader'] = _MINORBLOCKHEADER
DESCRIPTOR.message_types_by_name['AddRootBlockRequest'] = _ADDROOTBLOCKREQUEST
DESCRIPTOR.message_types_by_name['AddMinorBlockHeaderRequest'] = _ADDMINORBLOCKHEADERREQUEST
DESCRIPTOR.message_types_by_name['AddMinorBlockHeaderResponse'] = _ADDMINORBLOCKHEADERRESPONSE
DESCRIPTOR.message_types_by_name['SetRootChainConfirmedBlockResponse'] = _SETROOTCHAINCONFIRMEDBLOCKRESPONSE
DESCRIPTOR.message_types_by_name['FinalizeMinorBlockResponse'] = _FINALIZEMINORBLOCKRESPONSE
DESCRIPTOR.message_types_by_name['AddRootBlockResponse'] = _ADDROOTBLOCKRESPONSE
DESCRIPTOR.message_types_by_name['GetUnconfirmedHeaderRequest'] = _GETUNCONFIRMEDHEADERREQUEST
DESCRIPTOR.message_types_by_name['GetUnconfirmedHeaderResponse'] = _GETUNCONFIRMEDHEADERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetRootChainConfirmedBlockRequest = _reflection.GeneratedProtocolMessageType('SetRootChainConfirmedBlockRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETROOTCHAINCONFIRMEDBLOCKREQUEST,
  '__module__' : 'proto.cluster_pb2'
  # @@protoc_insertion_point(class_scope:cluster.SetRootChainConfirmedBlockRequest)
  })
_sym_db.RegisterMessage(SetRootChainConfirmedBlockRequest)

FinalizeMinorBlockRequest = _reflection.GeneratedProtocolMessageType('FinalizeMinorBlockRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINALIZEMINORBLOCKREQUEST,
  '__module__' : 'proto.cluster_pb2'
  # @@protoc_insertion_point(class_scope:cluster.FinalizeMinorBlockRequest)
  })
_sym_db.RegisterMessage(FinalizeMinorBlockRequest)

ClusterSlaveStatus = _reflection.GeneratedProtocolMessageType('ClusterSlaveStatus', (_message.Message,), {
  'DESCRIPTOR' : _CLUSTERSLAVESTATUS,
  '__module__' : 'proto.cluster_pb2'
  # @@protoc_insertion_point(class_scope:cluster.ClusterSlaveStatus)
  })
_sym_db.RegisterMessage(ClusterSlaveStatus)

MinorBlockHeader = _reflection.GeneratedProtocolMessageType('MinorBlockHeader', (_message.Message,), {
  'DESCRIPTOR' : _MINORBLOCKHEADER,
  '__module__' : 'proto.cluster_pb2'
  # @@protoc_insertion_point(class_scope:cluster.MinorBlockHeader)
  })
_sym_db.RegisterMessage(MinorBlockHeader)

AddRootBlockRequest = _reflection.GeneratedProtocolMessageType('AddRootBlockRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDROOTBLOCKREQUEST,
  '__module__' : 'proto.cluster_pb2'
  # @@protoc_insertion_point(class_scope:cluster.AddRootBlockRequest)
  })
_sym_db.RegisterMessage(AddRootBlockRequest)

AddMinorBlockHeaderRequest = _reflection.GeneratedProtocolMessageType('AddMinorBlockHeaderRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDMINORBLOCKHEADERREQUEST,
  '__module__' : 'proto.cluster_pb2'
  # @@protoc_insertion_point(class_scope:cluster.AddMinorBlockHeaderRequest)
  })
_sym_db.RegisterMessage(AddMinorBlockHeaderRequest)

AddMinorBlockHeaderResponse = _reflection.GeneratedProtocolMessageType('AddMinorBlockHeaderResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDMINORBLOCKHEADERRESPONSE,
  '__module__' : 'proto.cluster_pb2'
  # @@protoc_insertion_point(class_scope:cluster.AddMinorBlockHeaderResponse)
  })
_sym_db.RegisterMessage(AddMinorBlockHeaderResponse)

SetRootChainConfirmedBlockResponse = _reflection.GeneratedProtocolMessageType('SetRootChainConfirmedBlockResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETROOTCHAINCONFIRMEDBLOCKRESPONSE,
  '__module__' : 'proto.cluster_pb2'
  # @@protoc_insertion_point(class_scope:cluster.SetRootChainConfirmedBlockResponse)
  })
_sym_db.RegisterMessage(SetRootChainConfirmedBlockResponse)

FinalizeMinorBlockResponse = _reflection.GeneratedProtocolMessageType('FinalizeMinorBlockResponse', (_message.Message,), {
  'DESCRIPTOR' : _FINALIZEMINORBLOCKRESPONSE,
  '__module__' : 'proto.cluster_pb2'
  # @@protoc_insertion_point(class_scope:cluster.FinalizeMinorBlockResponse)
  })
_sym_db.RegisterMessage(FinalizeMinorBlockResponse)

AddRootBlockResponse = _reflection.GeneratedProtocolMessageType('AddRootBlockResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDROOTBLOCKRESPONSE,
  '__module__' : 'proto.cluster_pb2'
  # @@protoc_insertion_point(class_scope:cluster.AddRootBlockResponse)
  })
_sym_db.RegisterMessage(AddRootBlockResponse)

GetUnconfirmedHeaderRequest = _reflection.GeneratedProtocolMessageType('GetUnconfirmedHeaderRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUNCONFIRMEDHEADERREQUEST,
  '__module__' : 'proto.cluster_pb2'
  # @@protoc_insertion_point(class_scope:cluster.GetUnconfirmedHeaderRequest)
  })
_sym_db.RegisterMessage(GetUnconfirmedHeaderRequest)

GetUnconfirmedHeaderResponse = _reflection.GeneratedProtocolMessageType('GetUnconfirmedHeaderResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUNCONFIRMEDHEADERRESPONSE,
  '__module__' : 'proto.cluster_pb2'
  # @@protoc_insertion_point(class_scope:cluster.GetUnconfirmedHeaderResponse)
  })
_sym_db.RegisterMessage(GetUnconfirmedHeaderResponse)



_CLUSTERSLAVE = _descriptor.ServiceDescriptor(
  name='ClusterSlave',
  full_name='cluster.ClusterSlave',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=814,
  serialized_end=1228,
  methods=[
  _descriptor.MethodDescriptor(
    name='SetRootChainConfirmedBlock',
    full_name='cluster.ClusterSlave.SetRootChainConfirmedBlock',
    index=0,
    containing_service=None,
    input_type=_SETROOTCHAINCONFIRMEDBLOCKREQUEST,
    output_type=_SETROOTCHAINCONFIRMEDBLOCKRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FinalizeMinorBlock',
    full_name='cluster.ClusterSlave.FinalizeMinorBlock',
    index=1,
    containing_service=None,
    input_type=_FINALIZEMINORBLOCKREQUEST,
    output_type=_FINALIZEMINORBLOCKRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddRootBlock',
    full_name='cluster.ClusterSlave.AddRootBlock',
    index=2,
    containing_service=None,
    input_type=_ADDROOTBLOCKREQUEST,
    output_type=_ADDROOTBLOCKRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetUnconfirmedHeader',
    full_name='cluster.ClusterSlave.GetUnconfirmedHeader',
    index=3,
    containing_service=None,
    input_type=_GETUNCONFIRMEDHEADERREQUEST,
    output_type=_GETUNCONFIRMEDHEADERRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLUSTERSLAVE)

DESCRIPTOR.services_by_name['ClusterSlave'] = _CLUSTERSLAVE


_CLUSTERMASTER = _descriptor.ServiceDescriptor(
  name='ClusterMaster',
  full_name='cluster.ClusterMaster',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=1230,
  serialized_end=1345,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddMinorBlockHeader',
    full_name='cluster.ClusterMaster.AddMinorBlockHeader',
    index=0,
    containing_service=None,
    input_type=_ADDMINORBLOCKHEADERREQUEST,
    output_type=_ADDMINORBLOCKHEADERRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLUSTERMASTER)

DESCRIPTOR.services_by_name['ClusterMaster'] = _CLUSTERMASTER

# @@protoc_insertion_point(module_scope)
