# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: node.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\nnode.proto\x12\x04node\x1a\x1bgoogle/protobuf/empty.proto"m\n\x07Message\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0b\n\x03ttl\x18\x02 \x01(\x05\x12\x0c\n\x04hash\x18\x03 \x01(\x03\x12\x0b\n\x03\x63md\x18\x04 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x05 \x03(\t\x12\x12\n\x05round\x18\x06 \x01(\x05H\x00\x88\x01\x01\x42\x08\n\x06_round"_\n\x07Weights\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\r\n\x05round\x18\x02 \x01(\x05\x12\x0f\n\x07weights\x18\x03 \x01(\x0c\x12\x14\n\x0c\x63ontributors\x18\x04 \x03(\t\x12\x0e\n\x06weight\x18\x05 \x01(\x05" \n\x10HandShakeRequest\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x01(\t"/\n\x0fResponseMessage\x12\x12\n\x05\x65rror\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_error2\xf1\x01\n\x0cNodeServices\x12:\n\thandshake\x12\x16.node.HandShakeRequest\x1a\x15.node.ResponseMessage\x12<\n\ndisconnect\x12\x16.node.HandShakeRequest\x1a\x16.google.protobuf.Empty\x12\x34\n\x0csend_message\x12\r.node.Message\x1a\x15.node.ResponseMessage\x12\x31\n\tadd_model\x12\r.node.Weights\x1a\x15.node.ResponseMessageb\x06proto3'
)


_MESSAGE = DESCRIPTOR.message_types_by_name["Message"]
_WEIGHTS = DESCRIPTOR.message_types_by_name["Weights"]
_HANDSHAKEREQUEST = DESCRIPTOR.message_types_by_name["HandShakeRequest"]
_RESPONSEMESSAGE = DESCRIPTOR.message_types_by_name["ResponseMessage"]
Message = _reflection.GeneratedProtocolMessageType(
    "Message",
    (_message.Message,),
    {
        "DESCRIPTOR": _MESSAGE,
        "__module__": "node_pb2"
        # @@protoc_insertion_point(class_scope:node.Message)
    },
)
_sym_db.RegisterMessage(Message)

Weights = _reflection.GeneratedProtocolMessageType(
    "Weights",
    (_message.Message,),
    {
        "DESCRIPTOR": _WEIGHTS,
        "__module__": "node_pb2"
        # @@protoc_insertion_point(class_scope:node.Weights)
    },
)
_sym_db.RegisterMessage(Weights)

HandShakeRequest = _reflection.GeneratedProtocolMessageType(
    "HandShakeRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _HANDSHAKEREQUEST,
        "__module__": "node_pb2"
        # @@protoc_insertion_point(class_scope:node.HandShakeRequest)
    },
)
_sym_db.RegisterMessage(HandShakeRequest)

ResponseMessage = _reflection.GeneratedProtocolMessageType(
    "ResponseMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESPONSEMESSAGE,
        "__module__": "node_pb2"
        # @@protoc_insertion_point(class_scope:node.ResponseMessage)
    },
)
_sym_db.RegisterMessage(ResponseMessage)

_NODESERVICES = DESCRIPTOR.services_by_name["NodeServices"]
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _MESSAGE._serialized_start = 49
    _MESSAGE._serialized_end = 158
    _WEIGHTS._serialized_start = 160
    _WEIGHTS._serialized_end = 255
    _HANDSHAKEREQUEST._serialized_start = 257
    _HANDSHAKEREQUEST._serialized_end = 289
    _RESPONSEMESSAGE._serialized_start = 291
    _RESPONSEMESSAGE._serialized_end = 338
    _NODESERVICES._serialized_start = 341
    _NODESERVICES._serialized_end = 582
# @@protoc_insertion_point(module_scope)
