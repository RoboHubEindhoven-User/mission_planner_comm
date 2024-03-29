# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: robot_arm_pose.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='robot_arm_pose.proto',
  package='mission_protobuf',
  serialized_pb=_b('\n\x14robot_arm_pose.proto\x12\x10mission_protobuf\"\xb5\x01\n\x08RobotArm\x12-\n\x04pose\x18\x01 \x02(\x0b\x32\x1f.mission_protobuf.RobotArm.Pose\x1az\n\x04Pose\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0f\n\x07joint_1\x18\x02 \x02(\x01\x12\x0f\n\x07joint_2\x18\x03 \x02(\x01\x12\x0f\n\x07joint_3\x18\x04 \x02(\x01\x12\x0f\n\x07joint_4\x18\x05 \x02(\x01\x12\x0f\n\x07joint_5\x18\x06 \x02(\x01\x12\x0f\n\x07joint_6\x18\x07 \x02(\x01\"Q\n\x15RobotArmConfiguration\x12\n\n\x02id\x18\x01 \x02(\x05\x12,\n\x08\x61rm_pose\x18\x02 \x03(\x0b\x32\x1a.mission_protobuf.RobotArmB1\n\x1forg.mission_planner.common_msgsB\x0eRobotArmProtos')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ROBOTARM_POSE = _descriptor.Descriptor(
  name='Pose',
  full_name='mission_protobuf.RobotArm.Pose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mission_protobuf.RobotArm.Pose.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='joint_1', full_name='mission_protobuf.RobotArm.Pose.joint_1', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='joint_2', full_name='mission_protobuf.RobotArm.Pose.joint_2', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='joint_3', full_name='mission_protobuf.RobotArm.Pose.joint_3', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='joint_4', full_name='mission_protobuf.RobotArm.Pose.joint_4', index=4,
      number=5, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='joint_5', full_name='mission_protobuf.RobotArm.Pose.joint_5', index=5,
      number=6, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='joint_6', full_name='mission_protobuf.RobotArm.Pose.joint_6', index=6,
      number=7, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=102,
  serialized_end=224,
)

_ROBOTARM = _descriptor.Descriptor(
  name='RobotArm',
  full_name='mission_protobuf.RobotArm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pose', full_name='mission_protobuf.RobotArm.pose', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ROBOTARM_POSE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=224,
)


_ROBOTARMCONFIGURATION = _descriptor.Descriptor(
  name='RobotArmConfiguration',
  full_name='mission_protobuf.RobotArmConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mission_protobuf.RobotArmConfiguration.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arm_pose', full_name='mission_protobuf.RobotArmConfiguration.arm_pose', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=226,
  serialized_end=307,
)

_ROBOTARM_POSE.containing_type = _ROBOTARM
_ROBOTARM.fields_by_name['pose'].message_type = _ROBOTARM_POSE
_ROBOTARMCONFIGURATION.fields_by_name['arm_pose'].message_type = _ROBOTARM
DESCRIPTOR.message_types_by_name['RobotArm'] = _ROBOTARM
DESCRIPTOR.message_types_by_name['RobotArmConfiguration'] = _ROBOTARMCONFIGURATION

RobotArm = _reflection.GeneratedProtocolMessageType('RobotArm', (_message.Message,), dict(

  Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), dict(
    DESCRIPTOR = _ROBOTARM_POSE,
    __module__ = 'robot_arm_pose_pb2'
    # @@protoc_insertion_point(class_scope:mission_protobuf.RobotArm.Pose)
    ))
  ,
  DESCRIPTOR = _ROBOTARM,
  __module__ = 'robot_arm_pose_pb2'
  # @@protoc_insertion_point(class_scope:mission_protobuf.RobotArm)
  ))
_sym_db.RegisterMessage(RobotArm)
_sym_db.RegisterMessage(RobotArm.Pose)

RobotArmConfiguration = _reflection.GeneratedProtocolMessageType('RobotArmConfiguration', (_message.Message,), dict(
  DESCRIPTOR = _ROBOTARMCONFIGURATION,
  __module__ = 'robot_arm_pose_pb2'
  # @@protoc_insertion_point(class_scope:mission_protobuf.RobotArmConfiguration)
  ))
_sym_db.RegisterMessage(RobotArmConfiguration)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\037org.mission_planner.common_msgsB\016RobotArmProtos'))
# @@protoc_insertion_point(module_scope)
