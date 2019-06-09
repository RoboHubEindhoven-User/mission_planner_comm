#!/usr/bin/env python

'''
'''

__author__      = "Zinkeng Thierry"

from yaml import YAMLObject, SafeLoader

class JointPose(YAMLObject):
    yaml_loader = SafeLoader
    yaml_tag = u'!JointPose'
    
    def __init__(self, id = 0, description = "", joint_1 = 0, joint_2 = 0, joint_3 = 0, joint_4 = 0, joint_5 = 0, joint_6 = 0):
        self.id          = id
        self.description = description
        self.joint_1     = joint_1
        self.joint_2     = joint_2
        self.joint_3     = joint_3
        self.joint_4     = joint_4
        self.joint_5     = joint_5
        self.joint_6     = joint_6