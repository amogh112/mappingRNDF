# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from art_msgs/PilotBehavior.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class PilotBehavior(genpy.Message):
  _md5sum = "ee280e8dd8b427f32f9742e8b4885525"
  _type = "art_msgs/PilotBehavior"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# ART autonomous vehicle pilot node behaviors.
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
  # Pseudo-constants
  Run = 0
  Pause = 1
  Off = 2
  N_behaviors = 3

  __slots__ = ['value']
  _slot_types = ['uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       value

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PilotBehavior, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.value is None:
        self.value = 0
    else:
      self.value = 0

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
      buff.write(_struct_B.pack(self.value))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 1
      (self.value,) = _struct_B.unpack(str[start:end])
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
      buff.write(_struct_B.pack(self.value))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 1
      (self.value,) = _struct_B.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B = struct.Struct("<B")
