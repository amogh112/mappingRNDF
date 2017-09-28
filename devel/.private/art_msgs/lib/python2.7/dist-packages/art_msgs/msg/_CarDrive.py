# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from art_msgs/CarDrive.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import art_msgs.msg

class CarDrive(genpy.Message):
  _md5sum = "977b12f7daeec4c2a2276732baf95662"
  _type = "art_msgs/CarDrive"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Driving command for a car-like vehicle using Ackermann steering.
# $Id$

# Drive at requested speed, acceleration and jerk (the 1st, 2nd and
# 3rd derivatives of position). All are non-negative scalars. 
#
# Speed is defined as the scalar magnitude of the velocity
# vector. Direction (forwards or backwards) is determined by the gear.
#
# Zero acceleration means change speed as quickly as
# possible. Positive acceleration may include deceleration as needed
# to match the desired speed. It represents a desired rate and also a
# limit not to exceed.
#
# Zero jerk means change acceleration as quickly as possible. Positive
# jerk describes the desired rate of acceleration change in both
# directions (positive and negative).
#
float32 speed                   # magnitude of velocity vector (m/s)
float32 acceleration            # desired acceleration (m/s^2)
float32 jerk                    # desired jerk (m/s^3)

# Assumes Ackermann (front-wheel) steering. This angle is the average
# yaw of the two front wheels in the vehicle frame of reference
# (positive left), ignoring their slightly differing angles as if it
# were a tricycle. This is *not* the angle of the steering wheel
# inside the passenger compartment.
#
float32 steering_angle          # steering angle (radians)

Gear gear                       # requested gear (no change if Naught)
PilotBehavior behavior          # requested pilot behavior

================================================================================
MSG: art_msgs/Gear
# ART vehicle transmission gear numbers
#
# Used by several different messages.

# $Id$

# Gear numbers. 
#
# Naught means: reset all Shifter relays; no change of CarDrive gear.
uint8 Naught = 0
uint8 Park = 1
uint8 Reverse = 2
uint8 Neutral = 3
uint8 Drive = 4
uint8 N_gears = 5

uint8 value		# requested or reported gear number

================================================================================
MSG: art_msgs/PilotBehavior
# ART autonomous vehicle pilot node behaviors.
#
# Normally, the pilot node does Run, continually sending commands to
# the servo device actuators and monitoring their state.  With Pause,
# the pilot becomes passive, allowing a learning algorithm or human
# controller direct access to those devices.  In the Off state,
# various devices are shut down: the transmission in Park, the brake
# released, the throttle at idle.  The engine is not turned off, but
# it could be.

# $Id$

# Behavior value
uint8 value

# Behavior numbers:
uint8 Run = 0                   # normal driving
uint8 Pause = 1                 # stop issuing servo commands
uint8 Off = 2                   # turn off devices
uint8 N_behaviors = 3
"""
  __slots__ = ['speed','acceleration','jerk','steering_angle','gear','behavior']
  _slot_types = ['float32','float32','float32','float32','art_msgs/Gear','art_msgs/PilotBehavior']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       speed,acceleration,jerk,steering_angle,gear,behavior

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CarDrive, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.speed is None:
        self.speed = 0.
      if self.acceleration is None:
        self.acceleration = 0.
      if self.jerk is None:
        self.jerk = 0.
      if self.steering_angle is None:
        self.steering_angle = 0.
      if self.gear is None:
        self.gear = art_msgs.msg.Gear()
      if self.behavior is None:
        self.behavior = art_msgs.msg.PilotBehavior()
    else:
      self.speed = 0.
      self.acceleration = 0.
      self.jerk = 0.
      self.steering_angle = 0.
      self.gear = art_msgs.msg.Gear()
      self.behavior = art_msgs.msg.PilotBehavior()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_4f2B.pack(_x.speed, _x.acceleration, _x.jerk, _x.steering_angle, _x.gear.value, _x.behavior.value))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.gear is None:
        self.gear = art_msgs.msg.Gear()
      if self.behavior is None:
        self.behavior = art_msgs.msg.PilotBehavior()
      end = 0
      _x = self
      start = end
      end += 18
      (_x.speed, _x.acceleration, _x.jerk, _x.steering_angle, _x.gear.value, _x.behavior.value,) = _struct_4f2B.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_4f2B.pack(_x.speed, _x.acceleration, _x.jerk, _x.steering_angle, _x.gear.value, _x.behavior.value))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.gear is None:
        self.gear = art_msgs.msg.Gear()
      if self.behavior is None:
        self.behavior = art_msgs.msg.PilotBehavior()
      end = 0
      _x = self
      start = end
      end += 18
      (_x.speed, _x.acceleration, _x.jerk, _x.steering_angle, _x.gear.value, _x.behavior.value,) = _struct_4f2B.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4f2B = struct.Struct("<4f2B")
