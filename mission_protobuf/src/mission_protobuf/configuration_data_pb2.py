# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: configuration_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import task_action_pb2
import robot_arm_pose_pb2
import waypoint_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='configuration_data.proto',
  package='mission_protobuf',
  serialized_pb=_b('\n\x18\x63onfiguration_data.proto\x12\x10mission_protobuf\x1a\x11task_action.proto\x1a\x14robot_arm_pose.proto\x1a\x0ewaypoint.proto\"\xab\x01\n\x11\x43onfigurationData\x12,\n\x08wapoints\x18\x01 \x03(\x0b\x32\x1a.mission_protobuf.Waypoint\x12\x33\n\x0frobot_arm_poses\x18\x02 \x03(\x0b\x32\x1a.mission_protobuf.RobotArm\x12\x33\n\x07objects\x18\x03 \x03(\x0b\x32\".mission_protobuf.ObjectIdentifierB:\n\x1forg.mission_planner.common_msgsB\x17\x43onfigurationDataProtos')
  ,
  dependencies=[task_action_pb2.DESCRIPTOR,robot_arm_pose_pb2.DESCRIPTOR,waypoint_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CONFIGURATIONDATA = _descriptor.Descriptor(
  name='ConfigurationData',
  full_name='mission_protobuf.ConfigurationData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wapoints', full_name='mission_protobuf.ConfigurationData.wapoints', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='robot_arm_poses', full_name='mission_protobuf.ConfigurationData.robot_arm_poses', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='objects', full_name='mission_protobuf.ConfigurationData.objects', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=275,
)

_CONFIGURATIONDATA.fields_by_name['wapoints'].message_type = waypoint_pb2._WAYPOINT
_CONFIGURATIONDATA.fields_by_name['robot_arm_poses'].message_type = robot_arm_pose_pb2._ROBOTARM
_CONFIGURATIONDATA.fields_by_name['objects'].message_type = task_action_pb2._OBJECTIDENTIFIER
DESCRIPTOR.message_types_by_name['ConfigurationData'] = _CONFIGURATIONDATA

ConfigurationData = _reflection.GeneratedProtocolMessageType('ConfigurationData', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATIONDATA,
  __module__ = 'configuration_data_pb2'
  # @@protoc_insertion_point(class_scope:mission_protobuf.ConfigurationData)
  ))
_sym_db.RegisterMessage(ConfigurationData)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\037org.mission_planner.common_msgsB\027ConfigurationDataProtos'))
# @@protoc_insertion_point(module_scope)
