#!/usr/bin/env python

'''
'''

__author__      = "Zinkeng Thierry"

from yaml import YAMLObject, SafeLoader
import geometry
import service_area

class Location:
    def __init__(self, loc_type = None, instance_id = None, description = None):
        self.type        = loc_type
        self.instance_id = instance_id
        self.description = description

class Waypoint(YAMLObject):
    yaml_loader = SafeLoader
    yaml_tag = u'!Waypoint'

    def __init__(self, location = None, pose = None, service_area = None):
        self.location     = location
        self.pose         = pose
        self.service_area = service_area

        