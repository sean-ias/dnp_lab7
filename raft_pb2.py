# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: raft.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nraft.proto\"&\n\x05\x45ntry\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x0f\n\x07\x63ommand\x18\x02 \x01(\t\"\x08\n\x06NoArgs\"_\n\x0fRequestVoteArgs\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x13\n\x0b\x63\x61ndidateId\x18\x02 \x01(\x05\x12\x14\n\x0clastLogIndex\x18\x03 \x01(\x05\x12\x13\n\x0blastLogTerm\x18\x04 \x01(\x05\"\x8d\x01\n\x11\x41ppendEntriesArgs\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x10\n\x08leaderId\x18\x02 \x01(\x05\x12\x14\n\x0cprevLogIndex\x18\x03 \x01(\x05\x12\x13\n\x0bprevLogTerm\x18\x04 \x01(\x05\x12\x17\n\x07\x65ntries\x18\x05 \x03(\x0b\x32\x06.Entry\x12\x14\n\x0cleaderCommit\x18\x06 \x01(\x05\".\n\x0eResultWithTerm\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x0e\n\x06result\x18\x02 \x01(\x08\" \n\x0c\x44urationArgs\x12\x10\n\x08\x64uration\x18\x01 \x01(\x05\"4\n\nLeaderResp\x12\x11\n\tleader_id\x18\x01 \x01(\x05\x12\x13\n\x0bleader_addr\x18\x02 \x01(\t\"&\n\nSetValArgs\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0b\n\x03val\x18\x02 \x01(\t\"\x18\n\tGetValArg\x12\x0b\n\x03key\x18\x01 \x01(\t\"\x1c\n\x0c\x43onditionArg\x12\x0c\n\x04\x63ond\x18\x01 \x01(\x08\",\n\x0fValConditionArg\x12\x0c\n\x04\x63ond\x18\x01 \x01(\x08\x12\x0b\n\x03val\x18\x02 \x01(\t2\x86\x02\n\x08RaftNode\x12\x30\n\x0bRequestVote\x12\x10.RequestVoteArgs\x1a\x0f.ResultWithTerm\x12\x34\n\rAppendEntries\x12\x12.AppendEntriesArgs\x1a\x0f.ResultWithTerm\x12!\n\tGetLeader\x12\x07.NoArgs\x1a\x0b.LeaderResp\x12!\n\x07Suspend\x12\r.DurationArgs\x1a\x07.NoArgs\x12$\n\x06SetVal\x12\x0b.SetValArgs\x1a\r.ConditionArg\x12&\n\x06GetVal\x12\n.GetValArg\x1a\x10.ValConditionArgb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'raft_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ENTRY._serialized_start=14
  _ENTRY._serialized_end=52
  _NOARGS._serialized_start=54
  _NOARGS._serialized_end=62
  _REQUESTVOTEARGS._serialized_start=64
  _REQUESTVOTEARGS._serialized_end=159
  _APPENDENTRIESARGS._serialized_start=162
  _APPENDENTRIESARGS._serialized_end=303
  _RESULTWITHTERM._serialized_start=305
  _RESULTWITHTERM._serialized_end=351
  _DURATIONARGS._serialized_start=353
  _DURATIONARGS._serialized_end=385
  _LEADERRESP._serialized_start=387
  _LEADERRESP._serialized_end=439
  _SETVALARGS._serialized_start=441
  _SETVALARGS._serialized_end=479
  _GETVALARG._serialized_start=481
  _GETVALARG._serialized_end=505
  _CONDITIONARG._serialized_start=507
  _CONDITIONARG._serialized_end=535
  _VALCONDITIONARG._serialized_start=537
  _VALCONDITIONARG._serialized_end=581
  _RAFTNODE._serialized_start=584
  _RAFTNODE._serialized_end=846
# @@protoc_insertion_point(module_scope)
