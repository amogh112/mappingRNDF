# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from art_msgs/ArtLanes.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import art_msgs.msg
import std_msgs.msg

class ArtLanes(genpy.Message):
  _md5sum = "384de56fb723b4265b396fcf86b17531"
  _type = "art_msgs/ArtLanes"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# ART lanes message
# $Id$

Header header
ArtQuadrilateral[] polygons

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: art_msgs/ArtQuadrilateral
# ART quadrilateral polygon
# $Id$

# Each of these polygons is a quadrilateral.  The four vertex points
# are ordered relative to the heading of the lane containing it.

geometry_msgs/Polygon poly
int32 bottom_left  = 0
int32 top_left     = 1
int32 top_right    = 2
int32 bottom_right = 3
int32 quad_size = 4

geometry_msgs/Point midpoint # Middle of the polygon

float32 heading         # average of right and left boundary headings
float32 length          # length of the polygon
int32 poly_id           # unique MapLanes ID

bool is_stop            # this poly has a stop waypoint
bool is_transition      # not a lane polygon, no waypoint
bool contains_way       # both start_way and end_way are the contained waypoint

MapID start_way
MapID end_way

LaneMarking left_boundary
LaneMarking right_boundary

================================================================================
MSG: geometry_msgs/Polygon
#A specification of a polygon where the first and last points are assumed to be connected
Point32[] points

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
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: art_msgs/MapID
# Road map identifier for segments, lanes and way-points.
# $Id$

uint16 NULL_ID = 65535

uint16 seg      # segment ID
uint16 lane     # lane ID
uint16 pt       # way-point ID

================================================================================
MSG: art_msgs/LaneMarking
# Route Network Definition File lane marking
# $Id$

int16 DOUBLE_YELLOW = 0
int16 SOLID_YELLOW = 1
int16 SOLID_WHITE = 2
int16 BROKEN_WHITE = 3
int16 UNDEFINED = 4

int16 lane_marking
"""
  __slots__ = ['header','polygons']
  _slot_types = ['std_msgs/Header','art_msgs/ArtQuadrilateral[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,polygons

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ArtLanes, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.polygons is None:
        self.polygons = []
    else:
      self.header = std_msgs.msg.Header()
      self.polygons = []

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
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.polygons)
      buff.write(_struct_I.pack(length))
      for val1 in self.polygons:
        _v1 = val1.poly
        length = len(_v1.points)
        buff.write(_struct_I.pack(length))
        for val3 in _v1.points:
          _x = val3
          buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
        _v2 = val1.midpoint
        _x = _v2
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _x = val1
        buff.write(_struct_2fi3B.pack(_x.heading, _x.length, _x.poly_id, _x.is_stop, _x.is_transition, _x.contains_way))
        _v3 = val1.start_way
        _x = _v3
        buff.write(_struct_3H.pack(_x.seg, _x.lane, _x.pt))
        _v4 = val1.end_way
        _x = _v4
        buff.write(_struct_3H.pack(_x.seg, _x.lane, _x.pt))
        _v5 = val1.left_boundary
        buff.write(_struct_h.pack(_v5.lane_marking))
        _v6 = val1.right_boundary
        buff.write(_struct_h.pack(_v6.lane_marking))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.polygons is None:
        self.polygons = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.polygons = []
      for i in range(0, length):
        val1 = art_msgs.msg.ArtQuadrilateral()
        _v7 = val1.poly
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v7.points = []
        for i in range(0, length):
          val3 = geometry_msgs.msg.Point32()
          _x = val3
          start = end
          end += 12
          (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
          _v7.points.append(val3)
        _v8 = val1.midpoint
        _x = _v8
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _x = val1
        start = end
        end += 15
        (_x.heading, _x.length, _x.poly_id, _x.is_stop, _x.is_transition, _x.contains_way,) = _struct_2fi3B.unpack(str[start:end])
        val1.is_stop = bool(val1.is_stop)
        val1.is_transition = bool(val1.is_transition)
        val1.contains_way = bool(val1.contains_way)
        _v9 = val1.start_way
        _x = _v9
        start = end
        end += 6
        (_x.seg, _x.lane, _x.pt,) = _struct_3H.unpack(str[start:end])
        _v10 = val1.end_way
        _x = _v10
        start = end
        end += 6
        (_x.seg, _x.lane, _x.pt,) = _struct_3H.unpack(str[start:end])
        _v11 = val1.left_boundary
        start = end
        end += 2
        (_v11.lane_marking,) = _struct_h.unpack(str[start:end])
        _v12 = val1.right_boundary
        start = end
        end += 2
        (_v12.lane_marking,) = _struct_h.unpack(str[start:end])
        self.polygons.append(val1)
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
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.polygons)
      buff.write(_struct_I.pack(length))
      for val1 in self.polygons:
        _v13 = val1.poly
        length = len(_v13.points)
        buff.write(_struct_I.pack(length))
        for val3 in _v13.points:
          _x = val3
          buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
        _v14 = val1.midpoint
        _x = _v14
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _x = val1
        buff.write(_struct_2fi3B.pack(_x.heading, _x.length, _x.poly_id, _x.is_stop, _x.is_transition, _x.contains_way))
        _v15 = val1.start_way
        _x = _v15
        buff.write(_struct_3H.pack(_x.seg, _x.lane, _x.pt))
        _v16 = val1.end_way
        _x = _v16
        buff.write(_struct_3H.pack(_x.seg, _x.lane, _x.pt))
        _v17 = val1.left_boundary
        buff.write(_struct_h.pack(_v17.lane_marking))
        _v18 = val1.right_boundary
        buff.write(_struct_h.pack(_v18.lane_marking))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.polygons is None:
        self.polygons = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.polygons = []
      for i in range(0, length):
        val1 = art_msgs.msg.ArtQuadrilateral()
        _v19 = val1.poly
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v19.points = []
        for i in range(0, length):
          val3 = geometry_msgs.msg.Point32()
          _x = val3
          start = end
          end += 12
          (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
          _v19.points.append(val3)
        _v20 = val1.midpoint
        _x = _v20
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _x = val1
        start = end
        end += 15
        (_x.heading, _x.length, _x.poly_id, _x.is_stop, _x.is_transition, _x.contains_way,) = _struct_2fi3B.unpack(str[start:end])
        val1.is_stop = bool(val1.is_stop)
        val1.is_transition = bool(val1.is_transition)
        val1.contains_way = bool(val1.contains_way)
        _v21 = val1.start_way
        _x = _v21
        start = end
        end += 6
        (_x.seg, _x.lane, _x.pt,) = _struct_3H.unpack(str[start:end])
        _v22 = val1.end_way
        _x = _v22
        start = end
        end += 6
        (_x.seg, _x.lane, _x.pt,) = _struct_3H.unpack(str[start:end])
        _v23 = val1.left_boundary
        start = end
        end += 2
        (_v23.lane_marking,) = _struct_h.unpack(str[start:end])
        _v24 = val1.right_boundary
        start = end
        end += 2
        (_v24.lane_marking,) = _struct_h.unpack(str[start:end])
        self.polygons.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_h = struct.Struct("<h")
_struct_2fi3B = struct.Struct("<2fi3B")
_struct_3I = struct.Struct("<3I")
_struct_3H = struct.Struct("<3H")
_struct_3f = struct.Struct("<3f")
_struct_3d = struct.Struct("<3d")
