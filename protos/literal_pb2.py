# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/literal.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14protos/literal.proto\x12\x06protos\x1a\x1egoogle/protobuf/wrappers.proto\"\x9e\x02\n\tIdLiteral\x12$\n\x04type\x18\x01 \x01(\x0e\x32\x16.protos.IdLiteral.Type\x12/\n\tid_column\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05\x61lias\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x04long\x18\x65 \x01(\x0b\x32\x1c.google.protobuf.UInt64ValueH\x00\x12.\n\x06string\x18\x66 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\")\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04LONG\x10\x01\x12\n\n\x06STRING\x10\x02\x42\x04\n\x02id\"\xa3\x03\n\x07Literal\x12!\n\x04type\x18\x01 \x01(\x0e\x32\x13.protos.LiteralType\x12,\n\x06string\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12)\n\x04long\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12,\n\x06\x64ouble\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12+\n\x07\x62oolean\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x11\n\ttimestamp\x18\x06 \x01(\x10\x12\x1d\n\x02id\x18\x07 \x01(\x0b\x32\x11.protos.IdLiteral\x12\x14\n\x0cstring_array\x18\x08 \x03(\t\x12\x12\n\nlong_array\x18\t \x03(\x03\x12\x14\n\x0c\x64ouble_array\x18\n \x03(\x01\x12\x13\n\x0b\x62ytes_array\x18\x0b \x03(\x0c\x12\x15\n\rboolean_array\x18\x0c \x03(\x08\x12#\n\x08id_array\x18\r \x03(\x0b\x32\x11.protos.IdLiteral\"R\n\x16LiteralTypeDescription\x12)\n\x0cliteral_type\x18\x01 \x01(\x0e\x32\x13.protos.LiteralType\x12\r\n\x05label\x18\x02 \x01(\t*\xda\x01\n\x0bLiteralType\x12\x0e\n\nUNKNOWN_LT\x10\x00\x12\n\n\x06STRING\x10\x01\x12\x08\n\x04LONG\x10\x02\x12\n\n\x06\x44OUBLE\x10\x03\x12\x0b\n\x07\x42OOLEAN\x10\x04\x12\r\n\tTIMESTAMP\x10\x05\x12\x06\n\x02ID\x10\x06\x12\x10\n\x0cSTRING_ARRAY\x10\x07\x12\x0e\n\nLONG_ARRAY\x10\x08\x12\x10\n\x0c\x44OUBLE_ARRAY\x10\t\x12\x11\n\rBOOLEAN_ARRAY\x10\n\x12\x0c\n\x08ID_ARRAY\x10\x0c\x12\x0f\n\x0bNULL_STRING\x10\r\x12\x0f\n\x0bNULL_NUMBER\x10\x0e\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.literal_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LITERALTYPE._serialized_start=860
  _LITERALTYPE._serialized_end=1078
  _IDLITERAL._serialized_start=65
  _IDLITERAL._serialized_end=351
  _IDLITERAL_TYPE._serialized_start=304
  _IDLITERAL_TYPE._serialized_end=345
  _LITERAL._serialized_start=354
  _LITERAL._serialized_end=773
  _LITERALTYPEDESCRIPTION._serialized_start=775
  _LITERALTYPEDESCRIPTION._serialized_end=857
# @@protoc_insertion_point(module_scope)
