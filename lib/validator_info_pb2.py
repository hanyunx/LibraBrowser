# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: validator_info.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='validator_info.proto',
  package='types',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x14validator_info.proto\x12\x05types\"\xaf\x01\n\rValidatorInfo\x12\x17\n\x0f\x61\x63\x63ount_address\x18\x01 \x01(\x0c\x12\x1c\n\x14\x63onsensus_public_key\x18\x02 \x01(\x0c\x12\x1e\n\x16\x63onsensus_voting_power\x18\x03 \x01(\x04\x12\"\n\x1anetwork_signing_public_key\x18\x04 \x01(\x0c\x12#\n\x1bnetwork_identity_public_key\x18\x05 \x01(\x0c\x62\x06proto3'
)




_VALIDATORINFO = _descriptor.Descriptor(
  name='ValidatorInfo',
  full_name='types.ValidatorInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_address', full_name='types.ValidatorInfo.account_address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='consensus_public_key', full_name='types.ValidatorInfo.consensus_public_key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='consensus_voting_power', full_name='types.ValidatorInfo.consensus_voting_power', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_signing_public_key', full_name='types.ValidatorInfo.network_signing_public_key', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_identity_public_key', full_name='types.ValidatorInfo.network_identity_public_key', index=4,
      number=5, type=12, cpp_type=9, label=1,
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
  serialized_start=32,
  serialized_end=207,
)

DESCRIPTOR.message_types_by_name['ValidatorInfo'] = _VALIDATORINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ValidatorInfo = _reflection.GeneratedProtocolMessageType('ValidatorInfo', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATORINFO,
  '__module__' : 'validator_info_pb2'
  # @@protoc_insertion_point(class_scope:types.ValidatorInfo)
  })
_sym_db.RegisterMessage(ValidatorInfo)


# @@protoc_insertion_point(module_scope)
