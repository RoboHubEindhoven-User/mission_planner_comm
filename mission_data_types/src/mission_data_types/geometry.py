#!/usr/bin/env python

'''
'''

__author__      = "Zinkeng Thierry"

from yaml import YAMLObject, SafeLoader

class Pose(YAMLObject):
    yaml_loader = SafeLoader
    yaml_tag = u'!Pose'

    def __init__(self, position = None, orientation = None):
        self.position    = position
        self.orientation = orientation
        
    class Point(YAMLObject):
        yaml_loader = SafeLoader
        yaml_tag = u'!Point'

        def __init__(self, x = None, y = None, z = None):
            self.x = x
            self.y = y
            self.z = z
    
    class Quaternion(YAMLObject):
        yaml_loader = SafeLoader
        yaml_tag = u'!Quaternion'

        def __init__(self, x = None, y = None, z = None, w = None):
            self.x = x
            self.y = y
            self.z = z
            self.w = w