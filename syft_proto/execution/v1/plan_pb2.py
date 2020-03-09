# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: syft_proto/execution/v1/plan.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft_proto.execution.v1 import computation_action_pb2 as syft__proto_dot_execution_dot_v1_dot_computation__action__pb2
from syft_proto.execution.v1 import state_pb2 as syft__proto_dot_execution_dot_v1_dot_state__pb2
from syft_proto.frameworks.torch.tensors.interpreters.v1 import placeholder_pb2 as syft__proto_dot_frameworks_dot_torch_dot_tensors_dot_interpreters_dot_v1_dot_placeholder__pb2
from syft_proto.types.syft.v1 import id_pb2 as syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='syft_proto/execution/v1/plan.proto',
  package='syft_proto.execution.v1',
  syntax='proto3',
<<<<<<< HEAD
  serialized_options=_b('\n$org.openmined.syftproto.execution.v1'),
  serialized_pb=_b('\n\"syft_proto/execution/v1/plan.proto\x12\x17syft_proto.execution.v1\x1a\x30syft_proto/execution/v1/computation_action.proto\x1a#syft_proto/execution/v1/state.proto\x1a\x45syft_proto/frameworks/torch/tensors/interpreters/v1/placeholder.proto\x1a!syft_proto/types/syft/v1/id.proto\"\xa0\x03\n\x04Plan\x12,\n\x02id\x18\x01 \x01(\x0b\x32\x1c.syft_proto.types.syft.v1.IdR\x02id\x12\x44\n\x07\x61\x63tions\x18\x02 \x03(\x0b\x32*.syft_proto.execution.v1.ComputationActionR\x07\x61\x63tions\x12\x34\n\x05state\x18\x03 \x01(\x0b\x32\x1e.syft_proto.execution.v1.StateR\x05state\x12#\n\rinclude_state\x18\x04 \x01(\x08R\x0cincludeState\x12\x19\n\x08is_built\x18\x05 \x01(\x08R\x07isBuilt\x12\x12\n\x04name\x18\x06 \x01(\tR\x04name\x12\x12\n\x04tags\x18\x07 \x03(\tR\x04tags\x12 \n\x0b\x64\x65scription\x18\x08 \x01(\tR\x0b\x64\x65scription\x12\x64\n\x0cplaceholders\x18\t \x03(\x0b\x32@.syft_proto.frameworks.torch.tensors.interpreters.v1.PlaceholderR\x0cplaceholdersB&\n$org.openmined.syftproto.execution.v1b\x06proto3')
=======
  serialized_options=b'\n$org.openmined.syftproto.execution.v1',
  serialized_pb=b'\n\"syft_proto/execution/v1/plan.proto\x12\x17syft_proto.execution.v1\x1a\x30syft_proto/execution/v1/computation_action.proto\x1a#syft_proto/execution/v1/state.proto\x1a\x45syft_proto/frameworks/torch/tensors/interpreters/v1/placeholder.proto\x1a!syft_proto/types/syft/v1/id.proto\"\xa0\x03\n\x04Plan\x12,\n\x02id\x18\x01 \x01(\x0b\x32\x1c.syft_proto.types.syft.v1.IdR\x02id\x12\x44\n\x07\x61\x63tions\x18\x02 \x03(\x0b\x32*.syft_proto.execution.v1.ComputationActionR\x07\x61\x63tions\x12\x34\n\x05state\x18\x03 \x01(\x0b\x32\x1e.syft_proto.execution.v1.StateR\x05state\x12#\n\rinclude_state\x18\x04 \x01(\x08R\x0cincludeState\x12\x19\n\x08is_built\x18\x05 \x01(\x08R\x07isBuilt\x12\x12\n\x04name\x18\x06 \x01(\tR\x04name\x12\x12\n\x04tags\x18\x07 \x03(\tR\x04tags\x12 \n\x0b\x64\x65scription\x18\x08 \x01(\tR\x0b\x64\x65scription\x12\x64\n\x0cplaceholders\x18\t \x03(\x0b\x32@.syft_proto.frameworks.torch.tensors.interpreters.v1.PlaceholderR\x0cplaceholdersB&\n$org.openmined.syftproto.execution.v1b\x06proto3'
>>>>>>> add communication_action and communication_message
  ,
  dependencies=[syft__proto_dot_execution_dot_v1_dot_computation__action__pb2.DESCRIPTOR,syft__proto_dot_execution_dot_v1_dot_state__pb2.DESCRIPTOR,syft__proto_dot_frameworks_dot_torch_dot_tensors_dot_interpreters_dot_v1_dot_placeholder__pb2.DESCRIPTOR,syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2.DESCRIPTOR,])




_PLAN = _descriptor.Descriptor(
  name='Plan',
  full_name='syft_proto.execution.v1.Plan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='syft_proto.execution.v1.Plan.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actions', full_name='syft_proto.execution.v1.Plan.actions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='actions', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='syft_proto.execution.v1.Plan.state', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='state', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='include_state', full_name='syft_proto.execution.v1.Plan.include_state', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='includeState', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_built', full_name='syft_proto.execution.v1.Plan.is_built', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='isBuilt', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='syft_proto.execution.v1.Plan.name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='syft_proto.execution.v1.Plan.tags', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='tags', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='syft_proto.execution.v1.Plan.description', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='placeholders', full_name='syft_proto.execution.v1.Plan.placeholders', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='placeholders', file=DESCRIPTOR),
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
  serialized_start=257,
  serialized_end=673,
)

_PLAN.fields_by_name['id'].message_type = syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2._ID
_PLAN.fields_by_name['actions'].message_type = syft__proto_dot_execution_dot_v1_dot_computation__action__pb2._COMPUTATIONACTION
_PLAN.fields_by_name['state'].message_type = syft__proto_dot_execution_dot_v1_dot_state__pb2._STATE
_PLAN.fields_by_name['placeholders'].message_type = syft__proto_dot_frameworks_dot_torch_dot_tensors_dot_interpreters_dot_v1_dot_placeholder__pb2._PLACEHOLDER
DESCRIPTOR.message_types_by_name['Plan'] = _PLAN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Plan = _reflection.GeneratedProtocolMessageType('Plan', (_message.Message,), {
  'DESCRIPTOR' : _PLAN,
  '__module__' : 'syft_proto.execution.v1.plan_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.execution.v1.Plan)
  })
_sym_db.RegisterMessage(Plan)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
