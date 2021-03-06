# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: validator_change.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ledger_info_pb2 as ledger__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='validator_change.proto',
  package='types',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x16validator_change.proto\x12\x05types\x1a\x11ledger_info.proto\"d\n\x14ValidatorChangeProof\x12>\n\x15ledger_info_with_sigs\x18\x01 \x03(\x0b\x32\x1f.types.LedgerInfoWithSignatures\x12\x0c\n\x04more\x18\x02 \x01(\x08\x62\x06proto3'
  ,
  dependencies=[ledger__info__pb2.DESCRIPTOR,])




_VALIDATORCHANGEPROOF = _descriptor.Descriptor(
  name='ValidatorChangeProof',
  full_name='types.ValidatorChangeProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_info_with_sigs', full_name='types.ValidatorChangeProof.ledger_info_with_sigs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='more', full_name='types.ValidatorChangeProof.more', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=52,
  serialized_end=152,
)

_VALIDATORCHANGEPROOF.fields_by_name['ledger_info_with_sigs'].message_type = ledger__info__pb2._LEDGERINFOWITHSIGNATURES
DESCRIPTOR.message_types_by_name['ValidatorChangeProof'] = _VALIDATORCHANGEPROOF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ValidatorChangeProof = _reflection.GeneratedProtocolMessageType('ValidatorChangeProof', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATORCHANGEPROOF,
  '__module__' : 'validator_change_pb2'
  # @@protoc_insertion_point(class_scope:types.ValidatorChangeProof)
  })
_sym_db.RegisterMessage(ValidatorChangeProof)


# @@protoc_insertion_point(module_scope)
