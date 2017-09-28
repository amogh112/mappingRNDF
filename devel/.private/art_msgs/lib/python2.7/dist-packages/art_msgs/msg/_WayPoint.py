# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from art_msgs/WayPoint.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import art_msgs.msg

class WayPoint(genpy.Message):
  _md5sum = "93d7bd4ade2e33f8e836f5cd46c71e50"
  _type = "art_msgs/WayPoint"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Way-point attributes
# $Id$

float64 latitude			# latitude in degrees
float64 longitude			# longitude in degrees
geometry_msgs/Point32 mapxy		# MapXY position
MapID id				# way-point ID
uint16 index    			# parser index of waypoint

# way-point flags
bool is_entry                           # lane or zone exit point
bool is_exit				# lane or zone entry point
bool is_goal				# this is a goal checkpoint
bool is_lane_change			# change lanes after here
bool is_spot				# parking spot
bool is_stop				# stop line here
bool is_perimeter			# zone perimeter point
int32 checkpoint_id			# checkpoint ID or zero
float32 lane_width

================================================================================
MSG: geometry_msgs/Point32
# This contains the position of a point in free space(with 32 bits of precision).
# It is recommeded to use Point wherever possible instead of Point32.  
# 
# This recommendation is to promote interoperability.  
#
# This message is designed to take up less space when sending
# lots of points at once, as in the case of a PointCloud.  

float32 x
float32 y
float32 z
================================================================================
MSG: art_msgs/MapID
# Road map identifier for segments, lanes and way-points.
# $Id$

uint16 NULL_ID = 65535

uint16 seg      # segment ID
uint16 lane     # lane ID
uint16 pt       # way-point ID
"""
  __slots__ = ['latitude','longitude','mapxy','id','index','is_entry','is_exit','is_goal','is_lane_change','is_spot','is_stop','is_perimeter','checkpoint_id','lane_width']
  _slot_types = ['float64','float64','geometry_msgs/Point32','art_msgs/MapID','uint16','bool','bool','bool','bool','bool','bool','bool','int32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       latitude,longitude,mapxy,id,index,is_entry,is_exit,is_goal,is_lane_change,is_spot,is_stop,is_perimeter,checkpoint_id,lane_width

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(WayPoint, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.latitude is None:
        self.latitude = 0.
      if self.longitude is None:
        self.longitude = 0.
      if self.mapxy is None:
        self.mapxy = geometry_msgs.msg.Point32()
      if self.id is None:
        self.id = art_msgs.msg.MapID()
      if self.index is None:
        self.index = 0
      if self.is_entry is None:
        self.is_entry = False
      if self.is_exit is None:
        self.is_exit = False
      if self.is_goal is None:
        self.is_goal = False
      if self.is_lane_change is None:
        self.is_lane_change = False
      if self.is_spot is None:
        self.is_spot = False
      if self.is_stop is None:
        self.is_stop = False
      if self.is_perimeter is None:
        self.is_perimeter = False
      if self.checkpoint_id is None:
        self.checkpoint_id = 0
      if self.lane_width is None:
        self.lane_width = 0.
    else:
      self.latitude = 0.
      self.longitude = 0.
      self.mapxy = geometry_msgs.msg.Point32()
      self.id = art_msgs.msg.MapID()
      self.index = 0
      self.is_entry = False
      self.is_exit = False
      self.is_goal = False
      self.is_lane_change = False
      self.is_spot = False
      self.is_stop = False
      self.is_perimeter = False
      self.checkpoint_id = 0
      self.lane_width = 0.

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
      buff.write(_struct_2d3f4H7Bif.pack(_x.latitude, _x.longitude, _x.mapxy.x, _x.mapxy.y, _x.mapxy.z, _x.id.seg, _x.id.lane, _x.id.pt, _x.index, _x.is_entry, _x.is_exit, _x.is_goal, _x.is_lane_change, _x.is_spot, _x.is_stop, _x.is_perimeter, _x.checkpoint_id, _x.lane_width))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.mapxy is None:
        self.mapxy = geometry_msgs.msg.Point32()
      if self.id is None:
        self.id = art_msgs.msg.MapID()
      end = 0
      _x = self
      start = end
      end += 51
      (_x.latitude, _x.longitude, _x.mapxy.x, _x.mapxy.y, _x.mapxy.z, _x.id.seg, _x.id.lane, _x.id.pt, _x.index, _x.is_entry, _x.is_exit, _x.is_goal, _x.is_lane_change, _x.is_spot, _x.is_stop, _x.is_perimeter, _x.checkpoint_id, _x.lane_width,) = _struct_2d3f4H7Bif.unpack(str[start:end])
      self.is_entry = bool(self.is_entry)
      self.is_exit = bool(self.is_exit)
      self.is_goal = bool(self.is_goal)
      self.is_lane_change = bool(self.is_lane_change)
      self.is_spot = bool(self.is_spot)
      self.is_stop = bool(self.is_stop)
      self.is_perimeter = bool(self.is_perimeter)
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
      buff.write(_struct_2d3f4H7Bif.pack(_x.latitude, _x.longitude, _x.mapxy.x, _x.mapxy.y, _x.mapxy.z, _x.id.seg, _x.id.lane, _x.id.pt, _x.index, _x.is_entry, _x.is_exit, _x.is_goal, _x.is_lane_change, _x.is_spot, _x.is_stop, _x.is_perimeter, _x.checkpoint_id, _x.lane_width))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.mapxy is None:
        self.mapxy = geometry_msgs.msg.Point32()
      if self.id is None:
        self.id = art_msgs.msg.MapID()
      end = 0
      _x = self
      start = end
      end += 51
      (_x.latitude, _x.longitude, _x.mapxy.x, _x.mapxy.y, _x.mapxy.z, _x.id.seg, _x.id.lane, _x.id.pt, _x.index, _x.is_entry, _x.is_exit, _x.is_goal, _x.is_lane_change, _x.is_spot, _x.is_stop, _x.is_perimeter, _x.checkpoint_id, _x.lane_width,) = _struct_2d3f4H7Bif.unpack(str[start:end])
      self.is_entry = bool(self.is_entry)
      self.is_exit = bool(self.is_exit)
      self.is_goal = bool(self.is_goal)
      self.is_lane_change = bool(self.is_lane_change)
      self.is_spot = bool(self.is_spot)
      self.is_stop = bool(self.is_stop)
      self.is_perimeter = bool(self.is_perimeter)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2d3f4H7Bif = struct.Struct("<2d3f4H7Bif")