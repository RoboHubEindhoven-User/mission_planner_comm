#!/usr/bin/env python

'''
'''

__author__      = "Zinkeng Thierry"

from yaml import YAMLObject, SafeLoader
import geometry

class ServiceArea(YAMLObject):
    yaml_loader = SafeLoader
    yaml_tag = u'!ServiceArea'

    def __init__(self, id = None, length = None, width = None, height = None, diameter = None, tilt_angle = None):
        self.id         = id
        self.length     = length
        self.width      = width
        self.height     = height
        self.diameter   = diameter
        self.tilt_angle = tilt_angle