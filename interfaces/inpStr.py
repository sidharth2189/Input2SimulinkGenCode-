from interfaces.otherLib import *

# Must define the structure.
class aStruct(Structure):

    _fields_ = [("x", c_double)]

# Example definition for array based structure
#class bStruct(Structure):
#
#    _fields_ = [("x", c_double),
#                ("y", c_double* 10),
#                ("z", c_bool* 5),
#        ]
