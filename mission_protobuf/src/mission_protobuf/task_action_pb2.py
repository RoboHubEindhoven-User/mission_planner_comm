# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task_action.proto

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
  name='task_action.proto',
  package='mission_protobuf',
  serialized_pb=_b('\n\x11task_action.proto\x12\x10mission_protobuf\"\xdf\x07\n\x10ObjectIdentifier\x12;\n\x04type\x18\x01 \x02(\x0e\x32-.mission_protobuf.ObjectIdentifier.ObjectType\x12\x0f\n\x07type_id\x18\x02 \x01(\x03\x12\x13\n\x0binstance_id\x18\x03 \x01(\x03\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x19\n\x11image_description\x18\x05 \x01(\t\"\xb7\x06\n\nObjectType\x12\x0c\n\x08\x46\x32\x30_20_B\x10\x01\x12\x0c\n\x08\x46\x32\x30_20_G\x10\x02\x12\x0c\n\x08S40_40_B\x10\x03\x12\x0c\n\x08S40_40_G\x10\x04\x12\x0b\n\x07M20_100\x10\x05\x12\x07\n\x03M20\x10\x06\x12\x07\n\x03M30\x10\x07\x12\x07\n\x03R20\x10\x08\x12\x0f\n\x0b\x42\x45\x41RING_BOX\x10\t\x12\x0b\n\x07\x42\x45\x41RING\x10\n\x12\x08\n\x04\x41XIS\x10\x0b\x12\x11\n\rDISTANCE_TUBE\x10\x0c\x12\t\n\x05MOTOR\x10\r\x12\x0f\n\x0b\x43ONTAINER_B\x10\x0e\x12\x0f\n\x0b\x43ONTAINER_R\x10\x0f\x12\x16\n\x12PICKUP_BLACK_WHITE\x10\x10\x12\x15\n\x11PICKUP_CHOCO_MILK\x10\x11\x12\x0f\n\x0b\x44UPLO_WHITE\x10\x12\x12\x11\n\rDUPLO_CLASSIC\x10\x13\x12\x14\n\x10TWIX_SPEKULATIUS\x10\x14\x12\x0e\n\nTWIX_WHITE\x10\x15\x12\x10\n\x0cTWIX_CLASSIC\x10\x16\x12\r\n\tTWIX_MINI\x10\x17\x12\x08\n\x04MARS\x10\x18\x12\r\n\tMARS_MINI\x10\x19\x12\x0c\n\x08SNICKERS\x10\x1a\x12\x11\n\rSNICKERS_MINI\x10\x1b\x12\x12\n\x0eKITKAT_CLASSIC\x10\x1c\x12\x10\n\x0cKITKAT_WHITE\x10\x1d\x12\x17\n\x13KITKAT_CHUNKY_WHITE\x10\x1e\x12\x19\n\x15KITKAT_CHUNKY_CLASSIC\x10\x1f\x12\x0f\n\x0bKITKAT_MINI\x10 \x12\x10\n\x0cLION_CLASSIC\x10!\x12\r\n\tLION_MINI\x10\"\x12\x0e\n\nM_M_CRIPSY\x10#\x12\x0e\n\nM_M_PEANUT\x10$\x12\n\n\x06\x42OUNTY\x10%\x12\x0f\n\x0b\x42OUNTY_MINI\x10&\x12\x0c\n\x08MILKYWAY\x10\'\x12\x11\n\rMILKYWAY_MINI\x10(\x12\x15\n\x11RITTERSPORT_NUGAT\x10)\x12\x1b\n\x17RITTERSPORT_KNUSPERKEKS\x10*\x12\x17\n\x13RITTERSPORT_JOGHURT\x10+\x12\x1d\n\x19RITTERSPORT_KNUSPERFLAKES\x10,\x12\x1d\n\x19RITTERSPORT_NUSS_SPLITTER\x10-\x12\x18\n\x14RITTERSPORT_MARZIPAN\x10.\"U\n\x13ObjectConfiguration\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x32\n\x06object\x18\x02 \x03(\x0b\x32\".mission_protobuf.ObjectIdentifier\"\xe5\x01\n\x12LocationIdentifier\x12?\n\x04type\x18\x01 \x02(\x0e\x32\x31.mission_protobuf.LocationIdentifier.LocationType\x12\x13\n\x0binstance_id\x18\x02 \x02(\x05\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"d\n\x0cLocationType\x12\x11\n\x04NONE\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x06\n\x02\x45N\x10\x00\x12\x06\n\x02SH\x10\x01\x12\x06\n\x02WS\x10\x02\x12\x06\n\x02\x43\x42\x10\x03\x12\x06\n\x02WP\x10\x04\x12\x06\n\x02PP\x10\x05\x12\t\n\x05ROBOT\x10\x06\x12\x06\n\x02\x45X\x10\x64\"\xcc\x02\n\tInventory\x12/\n\x05items\x18\x01 \x03(\x0b\x32 .mission_protobuf.Inventory.Item\x1a\xe4\x01\n\x04Item\x12\x32\n\x06object\x18\x01 \x02(\x0b\x32\".mission_protobuf.ObjectIdentifier\x12\x10\n\x08quantity\x18\x02 \x01(\x04\x12\x35\n\tcontainer\x18\x03 \x01(\x0b\x32\".mission_protobuf.ObjectIdentifier\x12\x36\n\x08location\x18\x04 \x01(\x0b\x32$.mission_protobuf.LocationIdentifier\"\'\n\x08\x43ompType\x12\x0c\n\x07\x43OMP_ID\x10\xd0\x0f\x12\r\n\x08MSG_TYPE\x10\xcb\x01\"\'\n\x08\x43ompType\x12\x0c\n\x07\x43OMP_ID\x10\xd0\x0f\x12\r\n\x08MSG_TYPE\x10\xc8\x01\"\xd0\x02\n\x0bTransaction\x12\x16\n\x0etransaction_id\x18\x01 \x02(\x04\x12\x10\n\x08order_id\x18\x02 \x02(\x04\x12\x32\n\x06object\x18\x03 \x02(\x0b\x32\".mission_protobuf.ObjectIdentifier\x12\x10\n\x08quantity\x18\x04 \x01(\r\x12\x34\n\x06\x61\x63tion\x18\x05 \x02(\x0e\x32$.mission_protobuf.Transaction.Action\x12\x34\n\x06source\x18\x06 \x01(\x0b\x32$.mission_protobuf.LocationIdentifier\x12\x39\n\x0b\x64\x65stination\x18\x07 \x01(\x0b\x32$.mission_protobuf.LocationIdentifier\"*\n\x06\x41\x63tion\x12\n\n\x06INSERT\x10\x01\x12\n\n\x06REMOVE\x10\x02\x12\x08\n\x04MOVE\x10\x03\"n\n\x0eTransactionLog\x12\x33\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x1d.mission_protobuf.Transaction\"\'\n\x08\x43ompType\x12\x0c\n\x07\x43OMP_ID\x10\xd0\x0f\x12\r\n\x08MSG_TYPE\x10\xc9\x01\x42\x33\n\x1forg.mission_planner.common_msgsB\x10TaskActionProtos')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_OBJECTIDENTIFIER_OBJECTTYPE = _descriptor.EnumDescriptor(
  name='ObjectType',
  full_name='mission_protobuf.ObjectIdentifier.ObjectType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='F20_20_B', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='F20_20_G', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S40_40_B', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S40_40_G', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='M20_100', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='M20', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='M30', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='R20', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BEARING_BOX', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BEARING', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AXIS', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISTANCE_TUBE', index=11, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOTOR', index=12, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTAINER_B', index=13, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTAINER_R', index=14, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PICKUP_BLACK_WHITE', index=15, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PICKUP_CHOCO_MILK', index=16, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUPLO_WHITE', index=17, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUPLO_CLASSIC', index=18, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWIX_SPEKULATIUS', index=19, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWIX_WHITE', index=20, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWIX_CLASSIC', index=21, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWIX_MINI', index=22, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MARS', index=23, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MARS_MINI', index=24, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SNICKERS', index=25, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SNICKERS_MINI', index=26, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KITKAT_CLASSIC', index=27, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KITKAT_WHITE', index=28, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KITKAT_CHUNKY_WHITE', index=29, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KITKAT_CHUNKY_CLASSIC', index=30, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KITKAT_MINI', index=31, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LION_CLASSIC', index=32, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LION_MINI', index=33, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='M_M_CRIPSY', index=34, number=35,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='M_M_PEANUT', index=35, number=36,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOUNTY', index=36, number=37,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOUNTY_MINI', index=37, number=38,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MILKYWAY', index=38, number=39,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MILKYWAY_MINI', index=39, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RITTERSPORT_NUGAT', index=40, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RITTERSPORT_KNUSPERKEKS', index=41, number=42,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RITTERSPORT_JOGHURT', index=42, number=43,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RITTERSPORT_KNUSPERFLAKES', index=43, number=44,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RITTERSPORT_NUSS_SPLITTER', index=44, number=45,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RITTERSPORT_MARZIPAN', index=45, number=46,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=208,
  serialized_end=1031,
)
_sym_db.RegisterEnumDescriptor(_OBJECTIDENTIFIER_OBJECTTYPE)

_LOCATIONIDENTIFIER_LOCATIONTYPE = _descriptor.EnumDescriptor(
  name='LocationType',
  full_name='mission_protobuf.LocationIdentifier.LocationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=-1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EN', index=1, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SH', index=2, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WS', index=3, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CB', index=4, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WP', index=5, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PP', index=6, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROBOT', index=7, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EX', index=8, number=100,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1250,
  serialized_end=1350,
)
_sym_db.RegisterEnumDescriptor(_LOCATIONIDENTIFIER_LOCATIONTYPE)

_INVENTORY_ITEM_COMPTYPE = _descriptor.EnumDescriptor(
  name='CompType',
  full_name='mission_protobuf.Inventory.Item.CompType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COMP_ID', index=0, number=2000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSG_TYPE', index=1, number=203,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1605,
  serialized_end=1644,
)
_sym_db.RegisterEnumDescriptor(_INVENTORY_ITEM_COMPTYPE)

_INVENTORY_COMPTYPE = _descriptor.EnumDescriptor(
  name='CompType',
  full_name='mission_protobuf.Inventory.CompType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COMP_ID', index=0, number=2000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSG_TYPE', index=1, number=200,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1646,
  serialized_end=1685,
)
_sym_db.RegisterEnumDescriptor(_INVENTORY_COMPTYPE)

_TRANSACTION_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='mission_protobuf.Transaction.Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INSERT', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVE', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1982,
  serialized_end=2024,
)
_sym_db.RegisterEnumDescriptor(_TRANSACTION_ACTION)

_TRANSACTIONLOG_COMPTYPE = _descriptor.EnumDescriptor(
  name='CompType',
  full_name='mission_protobuf.TransactionLog.CompType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COMP_ID', index=0, number=2000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSG_TYPE', index=1, number=201,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2097,
  serialized_end=2136,
)
_sym_db.RegisterEnumDescriptor(_TRANSACTIONLOG_COMPTYPE)


_OBJECTIDENTIFIER = _descriptor.Descriptor(
  name='ObjectIdentifier',
  full_name='mission_protobuf.ObjectIdentifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='mission_protobuf.ObjectIdentifier.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type_id', full_name='mission_protobuf.ObjectIdentifier.type_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='mission_protobuf.ObjectIdentifier.instance_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='mission_protobuf.ObjectIdentifier.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_description', full_name='mission_protobuf.ObjectIdentifier.image_description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OBJECTIDENTIFIER_OBJECTTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=1031,
)


_OBJECTCONFIGURATION = _descriptor.Descriptor(
  name='ObjectConfiguration',
  full_name='mission_protobuf.ObjectConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mission_protobuf.ObjectConfiguration.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object', full_name='mission_protobuf.ObjectConfiguration.object', index=1,
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
  serialized_start=1033,
  serialized_end=1118,
)


_LOCATIONIDENTIFIER = _descriptor.Descriptor(
  name='LocationIdentifier',
  full_name='mission_protobuf.LocationIdentifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='mission_protobuf.LocationIdentifier.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='mission_protobuf.LocationIdentifier.instance_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='mission_protobuf.LocationIdentifier.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LOCATIONIDENTIFIER_LOCATIONTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1121,
  serialized_end=1350,
)


_INVENTORY_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='mission_protobuf.Inventory.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object', full_name='mission_protobuf.Inventory.Item.object', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='mission_protobuf.Inventory.Item.quantity', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='container', full_name='mission_protobuf.Inventory.Item.container', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='mission_protobuf.Inventory.Item.location', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INVENTORY_ITEM_COMPTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1416,
  serialized_end=1644,
)

_INVENTORY = _descriptor.Descriptor(
  name='Inventory',
  full_name='mission_protobuf.Inventory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='mission_protobuf.Inventory.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_INVENTORY_ITEM, ],
  enum_types=[
    _INVENTORY_COMPTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1353,
  serialized_end=1685,
)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='mission_protobuf.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='mission_protobuf.Transaction.transaction_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='mission_protobuf.Transaction.order_id', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object', full_name='mission_protobuf.Transaction.object', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='mission_protobuf.Transaction.quantity', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='mission_protobuf.Transaction.action', index=4,
      number=5, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='mission_protobuf.Transaction.source', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='destination', full_name='mission_protobuf.Transaction.destination', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRANSACTION_ACTION,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1688,
  serialized_end=2024,
)


_TRANSACTIONLOG = _descriptor.Descriptor(
  name='TransactionLog',
  full_name='mission_protobuf.TransactionLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactions', full_name='mission_protobuf.TransactionLog.transactions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRANSACTIONLOG_COMPTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2026,
  serialized_end=2136,
)

_OBJECTIDENTIFIER.fields_by_name['type'].enum_type = _OBJECTIDENTIFIER_OBJECTTYPE
_OBJECTIDENTIFIER_OBJECTTYPE.containing_type = _OBJECTIDENTIFIER
_OBJECTCONFIGURATION.fields_by_name['object'].message_type = _OBJECTIDENTIFIER
_LOCATIONIDENTIFIER.fields_by_name['type'].enum_type = _LOCATIONIDENTIFIER_LOCATIONTYPE
_LOCATIONIDENTIFIER_LOCATIONTYPE.containing_type = _LOCATIONIDENTIFIER
_INVENTORY_ITEM.fields_by_name['object'].message_type = _OBJECTIDENTIFIER
_INVENTORY_ITEM.fields_by_name['container'].message_type = _OBJECTIDENTIFIER
_INVENTORY_ITEM.fields_by_name['location'].message_type = _LOCATIONIDENTIFIER
_INVENTORY_ITEM.containing_type = _INVENTORY
_INVENTORY_ITEM_COMPTYPE.containing_type = _INVENTORY_ITEM
_INVENTORY.fields_by_name['items'].message_type = _INVENTORY_ITEM
_INVENTORY_COMPTYPE.containing_type = _INVENTORY
_TRANSACTION.fields_by_name['object'].message_type = _OBJECTIDENTIFIER
_TRANSACTION.fields_by_name['action'].enum_type = _TRANSACTION_ACTION
_TRANSACTION.fields_by_name['source'].message_type = _LOCATIONIDENTIFIER
_TRANSACTION.fields_by_name['destination'].message_type = _LOCATIONIDENTIFIER
_TRANSACTION_ACTION.containing_type = _TRANSACTION
_TRANSACTIONLOG.fields_by_name['transactions'].message_type = _TRANSACTION
_TRANSACTIONLOG_COMPTYPE.containing_type = _TRANSACTIONLOG
DESCRIPTOR.message_types_by_name['ObjectIdentifier'] = _OBJECTIDENTIFIER
DESCRIPTOR.message_types_by_name['ObjectConfiguration'] = _OBJECTCONFIGURATION
DESCRIPTOR.message_types_by_name['LocationIdentifier'] = _LOCATIONIDENTIFIER
DESCRIPTOR.message_types_by_name['Inventory'] = _INVENTORY
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['TransactionLog'] = _TRANSACTIONLOG

ObjectIdentifier = _reflection.GeneratedProtocolMessageType('ObjectIdentifier', (_message.Message,), dict(
  DESCRIPTOR = _OBJECTIDENTIFIER,
  __module__ = 'task_action_pb2'
  # @@protoc_insertion_point(class_scope:mission_protobuf.ObjectIdentifier)
  ))
_sym_db.RegisterMessage(ObjectIdentifier)

ObjectConfiguration = _reflection.GeneratedProtocolMessageType('ObjectConfiguration', (_message.Message,), dict(
  DESCRIPTOR = _OBJECTCONFIGURATION,
  __module__ = 'task_action_pb2'
  # @@protoc_insertion_point(class_scope:mission_protobuf.ObjectConfiguration)
  ))
_sym_db.RegisterMessage(ObjectConfiguration)

LocationIdentifier = _reflection.GeneratedProtocolMessageType('LocationIdentifier', (_message.Message,), dict(
  DESCRIPTOR = _LOCATIONIDENTIFIER,
  __module__ = 'task_action_pb2'
  # @@protoc_insertion_point(class_scope:mission_protobuf.LocationIdentifier)
  ))
_sym_db.RegisterMessage(LocationIdentifier)

Inventory = _reflection.GeneratedProtocolMessageType('Inventory', (_message.Message,), dict(

  Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), dict(
    DESCRIPTOR = _INVENTORY_ITEM,
    __module__ = 'task_action_pb2'
    # @@protoc_insertion_point(class_scope:mission_protobuf.Inventory.Item)
    ))
  ,
  DESCRIPTOR = _INVENTORY,
  __module__ = 'task_action_pb2'
  # @@protoc_insertion_point(class_scope:mission_protobuf.Inventory)
  ))
_sym_db.RegisterMessage(Inventory)
_sym_db.RegisterMessage(Inventory.Item)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTION,
  __module__ = 'task_action_pb2'
  # @@protoc_insertion_point(class_scope:mission_protobuf.Transaction)
  ))
_sym_db.RegisterMessage(Transaction)

TransactionLog = _reflection.GeneratedProtocolMessageType('TransactionLog', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTIONLOG,
  __module__ = 'task_action_pb2'
  # @@protoc_insertion_point(class_scope:mission_protobuf.TransactionLog)
  ))
_sym_db.RegisterMessage(TransactionLog)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\037org.mission_planner.common_msgsB\020TaskActionProtos'))
# @@protoc_insertion_point(module_scope)