# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/transaction_info.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/transaction_info.proto',
  package='types',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1cproto/transaction_info.proto\x12\x05types\"\x85\x01\n\x0fTransactionInfo\x12\x18\n\x10transaction_hash\x18\x01 \x01(\x0c\x12\x17\n\x0fstate_root_hash\x18\x02 \x01(\x0c\x12\x17\n\x0f\x65vent_root_hash\x18\x03 \x01(\x0c\x12\x10\n\x08gas_used\x18\x04 \x01(\x04\x12\x14\n\x0cmajor_status\x18\x05 \x01(\x04\x62\x06proto3'
)




_TRANSACTIONINFO = _descriptor.Descriptor(
  name='TransactionInfo',
  full_name='types.TransactionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction_hash', full_name='types.TransactionInfo.transaction_hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state_root_hash', full_name='types.TransactionInfo.state_root_hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_root_hash', full_name='types.TransactionInfo.event_root_hash', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gas_used', full_name='types.TransactionInfo.gas_used', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='major_status', full_name='types.TransactionInfo.major_status', index=4,
      number=5, type=4, cpp_type=4, label=1,
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
  serialized_start=40,
  serialized_end=173,
)

DESCRIPTOR.message_types_by_name['TransactionInfo'] = _TRANSACTIONINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransactionInfo = _reflection.GeneratedProtocolMessageType('TransactionInfo', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONINFO,
  '__module__' : 'proto.transaction_info_pb2'
  # @@protoc_insertion_point(class_scope:types.TransactionInfo)
  })
_sym_db.RegisterMessage(TransactionInfo)


# @@protoc_insertion_point(module_scope)