# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: language_storage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='language_storage.proto',
  package='types',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x16language_storage.proto\x12\x05types\")\n\x08ModuleId\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\tb\x06proto3'
)




_MODULEID = _descriptor.Descriptor(
  name='ModuleId',
  full_name='types.ModuleId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='types.ModuleId.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='types.ModuleId.name', index=1,
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
  serialized_start=33,
  serialized_end=74,
)

DESCRIPTOR.message_types_by_name['ModuleId'] = _MODULEID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModuleId = _reflection.GeneratedProtocolMessageType('ModuleId', (_message.Message,), {
  'DESCRIPTOR' : _MODULEID,
  '__module__' : 'language_storage_pb2'
  # @@protoc_insertion_point(class_scope:types.ModuleId)
  })
_sym_db.RegisterMessage(ModuleId)


# @@protoc_insertion_point(module_scope)
