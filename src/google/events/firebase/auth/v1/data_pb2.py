# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/events/firebase/auth/v1/data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n)google/events/firebase/auth/v1/data.proto\x12\x1egoogle.events.firebase.auth.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc5\x02\n\rAuthEventData\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x16\n\x0e\x65mail_verified\x18\x03 \x01(\x08\x12\x14\n\x0c\x64isplay_name\x18\x04 \x01(\t\x12\x11\n\tphoto_URL\x18\x05 \x01(\t\x12\x10\n\x08\x64isabled\x18\x06 \x01(\x08\x12>\n\x08metadata\x18\x07 \x01(\x0b\x32,.google.events.firebase.auth.v1.UserMetadata\x12?\n\rprovider_data\x18\x08 \x03(\x0b\x32(.google.events.firebase.auth.v1.UserInfo\x12\x14\n\x0cphone_number\x18\t \x01(\t\x12.\n\rcustom_claims\x18\n \x01(\x0b\x32\x17.google.protobuf.Struct"v\n\x0cUserMetadata\x12/\n\x0b\x63reate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x11last_sign_in_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp"d\n\x08UserInfo\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12\x11\n\tphoto_URL\x18\x04 \x01(\t\x12\x13\n\x0bprovider_id\x18\x05 \x01(\tB*\xaa\x02\'Google.Events.Protobuf.Firebase.Auth.V1b\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "google.events.firebase.auth.v1.data_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\252\002'Google.Events.Protobuf.Firebase.Auth.V1"
    _AUTHEVENTDATA._serialized_start = 141
    _AUTHEVENTDATA._serialized_end = 466
    _USERMETADATA._serialized_start = 468
    _USERMETADATA._serialized_end = 586
    _USERINFO._serialized_start = 588
    _USERINFO._serialized_end = 688
# @@protoc_insertion_point(module_scope)
