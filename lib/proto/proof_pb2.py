# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/proof.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto import transaction_info_pb2 as proto_dot_transaction__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/proof.proto',
  package='types',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x11proto/proof.proto\x12\x05types\x1a\x1cproto/transaction_info.proto\"$\n\x10\x41\x63\x63umulatorProof\x12\x10\n\x08siblings\x18\x01 \x03(\x0c\"3\n\x11SparseMerkleProof\x12\x0c\n\x04leaf\x18\x01 \x01(\x0c\x12\x10\n\x08siblings\x18\x02 \x03(\x0c\"/\n\x1b\x41\x63\x63umulatorConsistencyProof\x12\x10\n\x08subtrees\x18\x01 \x03(\x0c\"F\n\x15\x41\x63\x63umulatorRangeProof\x12\x15\n\rleft_siblings\x18\x01 \x03(\x0c\x12\x16\n\x0eright_siblings\x18\x02 \x03(\x0c\"0\n\x16SparseMerkleRangeProof\x12\x16\n\x0eright_siblings\x18\x01 \x03(\x0c\"\x8c\x01\n\x10TransactionProof\x12\x46\n%ledger_info_to_transaction_info_proof\x18\x01 \x01(\x0b\x32\x17.types.AccumulatorProof\x12\x30\n\x10transaction_info\x18\x02 \x01(\x0b\x32\x16.types.TransactionInfo\"\xd2\x01\n\x11\x41\x63\x63ountStateProof\x12\x46\n%ledger_info_to_transaction_info_proof\x18\x01 \x01(\x0b\x32\x17.types.AccumulatorProof\x12\x30\n\x10transaction_info\x18\x02 \x01(\x0b\x32\x16.types.TransactionInfo\x12\x43\n!transaction_info_to_account_proof\x18\x03 \x01(\x0b\x32\x18.types.SparseMerkleProof\"\xc8\x01\n\nEventProof\x12\x46\n%ledger_info_to_transaction_info_proof\x18\x01 \x01(\x0b\x32\x17.types.AccumulatorProof\x12\x30\n\x10transaction_info\x18\x02 \x01(\x0b\x32\x16.types.TransactionInfo\x12@\n\x1ftransaction_info_to_event_proof\x18\x03 \x01(\x0b\x32\x17.types.AccumulatorProof\"\x97\x01\n\x14TransactionListProof\x12L\n&ledger_info_to_transaction_infos_proof\x18\x01 \x01(\x0b\x32\x1c.types.AccumulatorRangeProof\x12\x31\n\x11transaction_infos\x18\x02 \x03(\x0b\x32\x16.types.TransactionInfob\x06proto3'
  ,
  dependencies=[proto_dot_transaction__info__pb2.DESCRIPTOR,])




_ACCUMULATORPROOF = _descriptor.Descriptor(
  name='AccumulatorProof',
  full_name='types.AccumulatorProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='siblings', full_name='types.AccumulatorProof.siblings', index=0,
      number=1, type=12, cpp_type=9, label=3,
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
  serialized_start=58,
  serialized_end=94,
)


_SPARSEMERKLEPROOF = _descriptor.Descriptor(
  name='SparseMerkleProof',
  full_name='types.SparseMerkleProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='leaf', full_name='types.SparseMerkleProof.leaf', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='siblings', full_name='types.SparseMerkleProof.siblings', index=1,
      number=2, type=12, cpp_type=9, label=3,
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
  serialized_start=96,
  serialized_end=147,
)


_ACCUMULATORCONSISTENCYPROOF = _descriptor.Descriptor(
  name='AccumulatorConsistencyProof',
  full_name='types.AccumulatorConsistencyProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='subtrees', full_name='types.AccumulatorConsistencyProof.subtrees', index=0,
      number=1, type=12, cpp_type=9, label=3,
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
  serialized_start=149,
  serialized_end=196,
)


_ACCUMULATORRANGEPROOF = _descriptor.Descriptor(
  name='AccumulatorRangeProof',
  full_name='types.AccumulatorRangeProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='left_siblings', full_name='types.AccumulatorRangeProof.left_siblings', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_siblings', full_name='types.AccumulatorRangeProof.right_siblings', index=1,
      number=2, type=12, cpp_type=9, label=3,
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
  serialized_start=198,
  serialized_end=268,
)


_SPARSEMERKLERANGEPROOF = _descriptor.Descriptor(
  name='SparseMerkleRangeProof',
  full_name='types.SparseMerkleRangeProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='right_siblings', full_name='types.SparseMerkleRangeProof.right_siblings', index=0,
      number=1, type=12, cpp_type=9, label=3,
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
  serialized_start=270,
  serialized_end=318,
)


_TRANSACTIONPROOF = _descriptor.Descriptor(
  name='TransactionProof',
  full_name='types.TransactionProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_info_to_transaction_info_proof', full_name='types.TransactionProof.ledger_info_to_transaction_info_proof', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_info', full_name='types.TransactionProof.transaction_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=321,
  serialized_end=461,
)


_ACCOUNTSTATEPROOF = _descriptor.Descriptor(
  name='AccountStateProof',
  full_name='types.AccountStateProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_info_to_transaction_info_proof', full_name='types.AccountStateProof.ledger_info_to_transaction_info_proof', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_info', full_name='types.AccountStateProof.transaction_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_info_to_account_proof', full_name='types.AccountStateProof.transaction_info_to_account_proof', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=464,
  serialized_end=674,
)


_EVENTPROOF = _descriptor.Descriptor(
  name='EventProof',
  full_name='types.EventProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_info_to_transaction_info_proof', full_name='types.EventProof.ledger_info_to_transaction_info_proof', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_info', full_name='types.EventProof.transaction_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_info_to_event_proof', full_name='types.EventProof.transaction_info_to_event_proof', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=677,
  serialized_end=877,
)


_TRANSACTIONLISTPROOF = _descriptor.Descriptor(
  name='TransactionListProof',
  full_name='types.TransactionListProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_info_to_transaction_infos_proof', full_name='types.TransactionListProof.ledger_info_to_transaction_infos_proof', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_infos', full_name='types.TransactionListProof.transaction_infos', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=880,
  serialized_end=1031,
)

_TRANSACTIONPROOF.fields_by_name['ledger_info_to_transaction_info_proof'].message_type = _ACCUMULATORPROOF
_TRANSACTIONPROOF.fields_by_name['transaction_info'].message_type = proto_dot_transaction__info__pb2._TRANSACTIONINFO
_ACCOUNTSTATEPROOF.fields_by_name['ledger_info_to_transaction_info_proof'].message_type = _ACCUMULATORPROOF
_ACCOUNTSTATEPROOF.fields_by_name['transaction_info'].message_type = proto_dot_transaction__info__pb2._TRANSACTIONINFO
_ACCOUNTSTATEPROOF.fields_by_name['transaction_info_to_account_proof'].message_type = _SPARSEMERKLEPROOF
_EVENTPROOF.fields_by_name['ledger_info_to_transaction_info_proof'].message_type = _ACCUMULATORPROOF
_EVENTPROOF.fields_by_name['transaction_info'].message_type = proto_dot_transaction__info__pb2._TRANSACTIONINFO
_EVENTPROOF.fields_by_name['transaction_info_to_event_proof'].message_type = _ACCUMULATORPROOF
_TRANSACTIONLISTPROOF.fields_by_name['ledger_info_to_transaction_infos_proof'].message_type = _ACCUMULATORRANGEPROOF
_TRANSACTIONLISTPROOF.fields_by_name['transaction_infos'].message_type = proto_dot_transaction__info__pb2._TRANSACTIONINFO
DESCRIPTOR.message_types_by_name['AccumulatorProof'] = _ACCUMULATORPROOF
DESCRIPTOR.message_types_by_name['SparseMerkleProof'] = _SPARSEMERKLEPROOF
DESCRIPTOR.message_types_by_name['AccumulatorConsistencyProof'] = _ACCUMULATORCONSISTENCYPROOF
DESCRIPTOR.message_types_by_name['AccumulatorRangeProof'] = _ACCUMULATORRANGEPROOF
DESCRIPTOR.message_types_by_name['SparseMerkleRangeProof'] = _SPARSEMERKLERANGEPROOF
DESCRIPTOR.message_types_by_name['TransactionProof'] = _TRANSACTIONPROOF
DESCRIPTOR.message_types_by_name['AccountStateProof'] = _ACCOUNTSTATEPROOF
DESCRIPTOR.message_types_by_name['EventProof'] = _EVENTPROOF
DESCRIPTOR.message_types_by_name['TransactionListProof'] = _TRANSACTIONLISTPROOF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccumulatorProof = _reflection.GeneratedProtocolMessageType('AccumulatorProof', (_message.Message,), {
  'DESCRIPTOR' : _ACCUMULATORPROOF,
  '__module__' : 'proto.proof_pb2'
  # @@protoc_insertion_point(class_scope:types.AccumulatorProof)
  })
_sym_db.RegisterMessage(AccumulatorProof)

SparseMerkleProof = _reflection.GeneratedProtocolMessageType('SparseMerkleProof', (_message.Message,), {
  'DESCRIPTOR' : _SPARSEMERKLEPROOF,
  '__module__' : 'proto.proof_pb2'
  # @@protoc_insertion_point(class_scope:types.SparseMerkleProof)
  })
_sym_db.RegisterMessage(SparseMerkleProof)

AccumulatorConsistencyProof = _reflection.GeneratedProtocolMessageType('AccumulatorConsistencyProof', (_message.Message,), {
  'DESCRIPTOR' : _ACCUMULATORCONSISTENCYPROOF,
  '__module__' : 'proto.proof_pb2'
  # @@protoc_insertion_point(class_scope:types.AccumulatorConsistencyProof)
  })
_sym_db.RegisterMessage(AccumulatorConsistencyProof)

AccumulatorRangeProof = _reflection.GeneratedProtocolMessageType('AccumulatorRangeProof', (_message.Message,), {
  'DESCRIPTOR' : _ACCUMULATORRANGEPROOF,
  '__module__' : 'proto.proof_pb2'
  # @@protoc_insertion_point(class_scope:types.AccumulatorRangeProof)
  })
_sym_db.RegisterMessage(AccumulatorRangeProof)

SparseMerkleRangeProof = _reflection.GeneratedProtocolMessageType('SparseMerkleRangeProof', (_message.Message,), {
  'DESCRIPTOR' : _SPARSEMERKLERANGEPROOF,
  '__module__' : 'proto.proof_pb2'
  # @@protoc_insertion_point(class_scope:types.SparseMerkleRangeProof)
  })
_sym_db.RegisterMessage(SparseMerkleRangeProof)

TransactionProof = _reflection.GeneratedProtocolMessageType('TransactionProof', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONPROOF,
  '__module__' : 'proto.proof_pb2'
  # @@protoc_insertion_point(class_scope:types.TransactionProof)
  })
_sym_db.RegisterMessage(TransactionProof)

AccountStateProof = _reflection.GeneratedProtocolMessageType('AccountStateProof', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTSTATEPROOF,
  '__module__' : 'proto.proof_pb2'
  # @@protoc_insertion_point(class_scope:types.AccountStateProof)
  })
_sym_db.RegisterMessage(AccountStateProof)

EventProof = _reflection.GeneratedProtocolMessageType('EventProof', (_message.Message,), {
  'DESCRIPTOR' : _EVENTPROOF,
  '__module__' : 'proto.proof_pb2'
  # @@protoc_insertion_point(class_scope:types.EventProof)
  })
_sym_db.RegisterMessage(EventProof)

TransactionListProof = _reflection.GeneratedProtocolMessageType('TransactionListProof', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONLISTPROOF,
  '__module__' : 'proto.proof_pb2'
  # @@protoc_insertion_point(class_scope:types.TransactionListProof)
  })
_sym_db.RegisterMessage(TransactionListProof)


# @@protoc_insertion_point(module_scope)