# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/playbooks/source_task_definitions/kubectl_task.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;protos/playbooks/source_task_definitions/kubectl_task.proto\x12\x10protos.playbooks\x1a\x1egoogle/protobuf/wrappers.proto\"\x9a\x01\n\x07Kubectl\x12\x30\n\x04type\x18\x01 \x01(\x0e\x32\".protos.playbooks.Kubectl.TaskType\x12/\n\x07\x63ommand\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\"$\n\x08TaskType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07\x43OMMAND\x10\x01\x42\x06\n\x04taskb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.playbooks.source_task_definitions.kubectl_task_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _KUBECTL._serialized_start=114
  _KUBECTL._serialized_end=268
  _KUBECTL_TASKTYPE._serialized_start=224
  _KUBECTL_TASKTYPE._serialized_end=260
# @@protoc_insertion_point(module_scope)
