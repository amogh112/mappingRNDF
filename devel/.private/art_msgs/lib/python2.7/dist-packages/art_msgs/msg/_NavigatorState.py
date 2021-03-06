# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from art_msgs/NavigatorState.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import art_msgs.msg
import std_msgs.msg

class NavigatorState(genpy.Message):
  _md5sum = "c40e5f1fdc1b82b80af736960035d5c8"
  _type = "art_msgs/NavigatorState"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# navigator state message
# $Id$

Header header

EstopState estop
RoadState road

art_msgs/MapID last_waypt		# last way-point reached
art_msgs/MapID replan_waypt		# next way-point for replan

int32 cur_poly                          # current polygon, -1 if none

# status flags
bool alarm
bool flasher
bool lane_blocked
bool road_blocked
bool reverse
bool signal_left
bool signal_right
bool stopped
bool have_zones

Order last_order			# last commander order received

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
MSG: art_msgs/EstopState
# Navigator E-stop state values
# $Id$

uint16 Pause    = 0			# E-stop pause (initial state)
uint16 Run      = 1			# E-stop run enabled
uint16 Done     = 2			# mission finished (disabled)
uint16 Suspend  = 3			# suspend autonomous operation
uint16 N_states = 4

uint16 state

================================================================================
MSG: art_msgs/RoadState
# Navigator Road state values
# $Id$

uint16 Init      = 0
uint16 Block     = 1
uint16 Evade     = 2
uint16 Follow    = 3
uint16 Pass      = 4
uint16 Uturn     = 5
uint16 WaitCross = 6
uint16 WaitLane  = 7
uint16 WaitPass  = 8
uint16 WaitStop  = 9
uint16 Zone      = 10
uint16 N_states  = 11

uint16 state

================================================================================
MSG: art_msgs/MapID
# Road map identifier for segments, lanes and way-points.
# $Id$

uint16 NULL_ID = 65535

uint16 seg      # segment ID
uint16 lane     # lane ID
uint16 pt       # way-point ID

================================================================================
MSG: art_msgs/Order
# commander order for the navigator
# $Id$

uint32 N_WAYPTS = 5     		# number of way-points in order
uint32 N_CHKPTS = 2             	# number of checkpoints in order

Behavior behavior			# requested behavior
art_msgs/WayPoint[5] waypt       	# way-point array
art_msgs/WayPoint[2] chkpt       	# next two goal checkpoints
float32 min_speed			# in meters/sec
float32 max_speed
int32 replan_num
int32 next_uturn         		# Uturn between [1] and [2]

================================================================================
MSG: art_msgs/Behavior
# ART Navigator behaviors (lower numbers have higher priority)
# $Id$

# enumerated behavior values
int16 Abort       = 0
int16 Quit        = 1
int16 Pause       = 2
int16 Run         = 3
int16 Suspend     = 4
int16 Initialize  = 5
int16 Go          = 6
int16 NONE        = 7
int16 N_behaviors = 8

int16 value

================================================================================
MSG: art_msgs/WayPoint
# Way-point attributes
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
float32 z"""
  __slots__ = ['header','estop','road','last_waypt','replan_waypt','cur_poly','alarm','flasher','lane_blocked','road_blocked','reverse','signal_left','signal_right','stopped','have_zones','last_order']
  _slot_types = ['std_msgs/Header','art_msgs/EstopState','art_msgs/RoadState','art_msgs/MapID','art_msgs/MapID','int32','bool','bool','bool','bool','bool','bool','bool','bool','bool','art_msgs/Order']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,estop,road,last_waypt,replan_waypt,cur_poly,alarm,flasher,lane_blocked,road_blocked,reverse,signal_left,signal_right,stopped,have_zones,last_order

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(NavigatorState, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.estop is None:
        self.estop = art_msgs.msg.EstopState()
      if self.road is None:
        self.road = art_msgs.msg.RoadState()
      if self.last_waypt is None:
        self.last_waypt = art_msgs.msg.MapID()
      if self.replan_waypt is None:
        self.replan_waypt = art_msgs.msg.MapID()
      if self.cur_poly is None:
        self.cur_poly = 0
      if self.alarm is None:
        self.alarm = False
      if self.flasher is None:
        self.flasher = False
      if self.lane_blocked is None:
        self.lane_blocked = False
      if self.road_blocked is None:
        self.road_blocked = False
      if self.reverse is None:
        self.reverse = False
      if self.signal_left is None:
        self.signal_left = False
      if self.signal_right is None:
        self.signal_right = False
      if self.stopped is None:
        self.stopped = False
      if self.have_zones is None:
        self.have_zones = False
      if self.last_order is None:
        self.last_order = art_msgs.msg.Order()
    else:
      self.header = std_msgs.msg.Header()
      self.estop = art_msgs.msg.EstopState()
      self.road = art_msgs.msg.RoadState()
      self.last_waypt = art_msgs.msg.MapID()
      self.replan_waypt = art_msgs.msg.MapID()
      self.cur_poly = 0
      self.alarm = False
      self.flasher = False
      self.lane_blocked = False
      self.road_blocked = False
      self.reverse = False
      self.signal_left = False
      self.signal_right = False
      self.stopped = False
      self.have_zones = False
      self.last_order = art_msgs.msg.Order()

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
      _x = self
      buff.write(_struct_8Hi9Bh.pack(_x.estop.state, _x.road.state, _x.last_waypt.seg, _x.last_waypt.lane, _x.last_waypt.pt, _x.replan_waypt.seg, _x.replan_waypt.lane, _x.replan_waypt.pt, _x.cur_poly, _x.alarm, _x.flasher, _x.lane_blocked, _x.road_blocked, _x.reverse, _x.signal_left, _x.signal_right, _x.stopped, _x.have_zones, _x.last_order.behavior.value))
      for val1 in self.last_order.waypt:
        _x = val1
        buff.write(_struct_2d.pack(_x.latitude, _x.longitude))
        _v1 = val1.mapxy
        _x = _v1
        buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
        _v2 = val1.id
        _x = _v2
        buff.write(_struct_3H.pack(_x.seg, _x.lane, _x.pt))
        _x = val1
        buff.write(_struct_H7Bif.pack(_x.index, _x.is_entry, _x.is_exit, _x.is_goal, _x.is_lane_change, _x.is_spot, _x.is_stop, _x.is_perimeter, _x.checkpoint_id, _x.lane_width))
      for val1 in self.last_order.chkpt:
        _x = val1
        buff.write(_struct_2d.pack(_x.latitude, _x.longitude))
        _v3 = val1.mapxy
        _x = _v3
        buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
        _v4 = val1.id
        _x = _v4
        buff.write(_struct_3H.pack(_x.seg, _x.lane, _x.pt))
        _x = val1
        buff.write(_struct_H7Bif.pack(_x.index, _x.is_entry, _x.is_exit, _x.is_goal, _x.is_lane_change, _x.is_spot, _x.is_stop, _x.is_perimeter, _x.checkpoint_id, _x.lane_width))
      _x = self
      buff.write(_struct_2f2i.pack(_x.last_order.min_speed, _x.last_order.max_speed, _x.last_order.replan_num, _x.last_order.next_uturn))
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
      if self.estop is None:
        self.estop = art_msgs.msg.EstopState()
      if self.road is None:
        self.road = art_msgs.msg.RoadState()
      if self.last_waypt is None:
        self.last_waypt = art_msgs.msg.MapID()
      if self.replan_waypt is None:
        self.replan_waypt = art_msgs.msg.MapID()
      if self.last_order is None:
        self.last_order = art_msgs.msg.Order()
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
      _x = self
      start = end
      end += 31
      (_x.estop.state, _x.road.state, _x.last_waypt.seg, _x.last_waypt.lane, _x.last_waypt.pt, _x.replan_waypt.seg, _x.replan_waypt.lane, _x.replan_waypt.pt, _x.cur_poly, _x.alarm, _x.flasher, _x.lane_blocked, _x.road_blocked, _x.reverse, _x.signal_left, _x.signal_right, _x.stopped, _x.have_zones, _x.last_order.behavior.value,) = _struct_8Hi9Bh.unpack(str[start:end])
      self.alarm = bool(self.alarm)
      self.flasher = bool(self.flasher)
      self.lane_blocked = bool(self.lane_blocked)
      self.road_blocked = bool(self.road_blocked)
      self.reverse = bool(self.reverse)
      self.signal_left = bool(self.signal_left)
      self.signal_right = bool(self.signal_right)
      self.stopped = bool(self.stopped)
      self.have_zones = bool(self.have_zones)
      self.last_order.waypt = []
      for i in range(0, 5):
        val1 = art_msgs.msg.WayPoint()
        _x = val1
        start = end
        end += 16
        (_x.latitude, _x.longitude,) = _struct_2d.unpack(str[start:end])
        _v5 = val1.mapxy
        _x = _v5
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
        _v6 = val1.id
        _x = _v6
        start = end
        end += 6
        (_x.seg, _x.lane, _x.pt,) = _struct_3H.unpack(str[start:end])
        _x = val1
        start = end
        end += 17
        (_x.index, _x.is_entry, _x.is_exit, _x.is_goal, _x.is_lane_change, _x.is_spot, _x.is_stop, _x.is_perimeter, _x.checkpoint_id, _x.lane_width,) = _struct_H7Bif.unpack(str[start:end])
        val1.is_entry = bool(val1.is_entry)
        val1.is_exit = bool(val1.is_exit)
        val1.is_goal = bool(val1.is_goal)
        val1.is_lane_change = bool(val1.is_lane_change)
        val1.is_spot = bool(val1.is_spot)
        val1.is_stop = bool(val1.is_stop)
        val1.is_perimeter = bool(val1.is_perimeter)
        self.last_order.waypt.append(val1)
      self.last_order.chkpt = []
      for i in range(0, 2):
        val1 = art_msgs.msg.WayPoint()
        _x = val1
        start = end
        end += 16
        (_x.latitude, _x.longitude,) = _struct_2d.unpack(str[start:end])
        _v7 = val1.mapxy
        _x = _v7
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
        _v8 = val1.id
        _x = _v8
        start = end
        end += 6
        (_x.seg, _x.lane, _x.pt,) = _struct_3H.unpack(str[start:end])
        _x = val1
        start = end
        end += 17
        (_x.index, _x.is_entry, _x.is_exit, _x.is_goal, _x.is_lane_change, _x.is_spot, _x.is_stop, _x.is_perimeter, _x.checkpoint_id, _x.lane_width,) = _struct_H7Bif.unpack(str[start:end])
        val1.is_entry = bool(val1.is_entry)
        val1.is_exit = bool(val1.is_exit)
        val1.is_goal = bool(val1.is_goal)
        val1.is_lane_change = bool(val1.is_lane_change)
        val1.is_spot = bool(val1.is_spot)
        val1.is_stop = bool(val1.is_stop)
        val1.is_perimeter = bool(val1.is_perimeter)
        self.last_order.chkpt.append(val1)
      _x = self
      start = end
      end += 16
      (_x.last_order.min_speed, _x.last_order.max_speed, _x.last_order.replan_num, _x.last_order.next_uturn,) = _struct_2f2i.unpack(str[start:end])
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
      _x = self
      buff.write(_struct_8Hi9Bh.pack(_x.estop.state, _x.road.state, _x.last_waypt.seg, _x.last_waypt.lane, _x.last_waypt.pt, _x.replan_waypt.seg, _x.replan_waypt.lane, _x.replan_waypt.pt, _x.cur_poly, _x.alarm, _x.flasher, _x.lane_blocked, _x.road_blocked, _x.reverse, _x.signal_left, _x.signal_right, _x.stopped, _x.have_zones, _x.last_order.behavior.value))
      for val1 in self.last_order.waypt:
        _x = val1
        buff.write(_struct_2d.pack(_x.latitude, _x.longitude))
        _v9 = val1.mapxy
        _x = _v9
        buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
        _v10 = val1.id
        _x = _v10
        buff.write(_struct_3H.pack(_x.seg, _x.lane, _x.pt))
        _x = val1
        buff.write(_struct_H7Bif.pack(_x.index, _x.is_entry, _x.is_exit, _x.is_goal, _x.is_lane_change, _x.is_spot, _x.is_stop, _x.is_perimeter, _x.checkpoint_id, _x.lane_width))
      for val1 in self.last_order.chkpt:
        _x = val1
        buff.write(_struct_2d.pack(_x.latitude, _x.longitude))
        _v11 = val1.mapxy
        _x = _v11
        buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
        _v12 = val1.id
        _x = _v12
        buff.write(_struct_3H.pack(_x.seg, _x.lane, _x.pt))
        _x = val1
        buff.write(_struct_H7Bif.pack(_x.index, _x.is_entry, _x.is_exit, _x.is_goal, _x.is_lane_change, _x.is_spot, _x.is_stop, _x.is_perimeter, _x.checkpoint_id, _x.lane_width))
      _x = self
      buff.write(_struct_2f2i.pack(_x.last_order.min_speed, _x.last_order.max_speed, _x.last_order.replan_num, _x.last_order.next_uturn))
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
      if self.estop is None:
        self.estop = art_msgs.msg.EstopState()
      if self.road is None:
        self.road = art_msgs.msg.RoadState()
      if self.last_waypt is None:
        self.last_waypt = art_msgs.msg.MapID()
      if self.replan_waypt is None:
        self.replan_waypt = art_msgs.msg.MapID()
      if self.last_order is None:
        self.last_order = art_msgs.msg.Order()
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
      _x = self
      start = end
      end += 31
      (_x.estop.state, _x.road.state, _x.last_waypt.seg, _x.last_waypt.lane, _x.last_waypt.pt, _x.replan_waypt.seg, _x.replan_waypt.lane, _x.replan_waypt.pt, _x.cur_poly, _x.alarm, _x.flasher, _x.lane_blocked, _x.road_blocked, _x.reverse, _x.signal_left, _x.signal_right, _x.stopped, _x.have_zones, _x.last_order.behavior.value,) = _struct_8Hi9Bh.unpack(str[start:end])
      self.alarm = bool(self.alarm)
      self.flasher = bool(self.flasher)
      self.lane_blocked = bool(self.lane_blocked)
      self.road_blocked = bool(self.road_blocked)
      self.reverse = bool(self.reverse)
      self.signal_left = bool(self.signal_left)
      self.signal_right = bool(self.signal_right)
      self.stopped = bool(self.stopped)
      self.have_zones = bool(self.have_zones)
      self.last_order.waypt = []
      for i in range(0, 5):
        val1 = art_msgs.msg.WayPoint()
        _x = val1
        start = end
        end += 16
        (_x.latitude, _x.longitude,) = _struct_2d.unpack(str[start:end])
        _v13 = val1.mapxy
        _x = _v13
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
        _v14 = val1.id
        _x = _v14
        start = end
        end += 6
        (_x.seg, _x.lane, _x.pt,) = _struct_3H.unpack(str[start:end])
        _x = val1
        start = end
        end += 17
        (_x.index, _x.is_entry, _x.is_exit, _x.is_goal, _x.is_lane_change, _x.is_spot, _x.is_stop, _x.is_perimeter, _x.checkpoint_id, _x.lane_width,) = _struct_H7Bif.unpack(str[start:end])
        val1.is_entry = bool(val1.is_entry)
        val1.is_exit = bool(val1.is_exit)
        val1.is_goal = bool(val1.is_goal)
        val1.is_lane_change = bool(val1.is_lane_change)
        val1.is_spot = bool(val1.is_spot)
        val1.is_stop = bool(val1.is_stop)
        val1.is_perimeter = bool(val1.is_perimeter)
        self.last_order.waypt.append(val1)
      self.last_order.chkpt = []
      for i in range(0, 2):
        val1 = art_msgs.msg.WayPoint()
        _x = val1
        start = end
        end += 16
        (_x.latitude, _x.longitude,) = _struct_2d.unpack(str[start:end])
        _v15 = val1.mapxy
        _x = _v15
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
        _v16 = val1.id
        _x = _v16
        start = end
        end += 6
        (_x.seg, _x.lane, _x.pt,) = _struct_3H.unpack(str[start:end])
        _x = val1
        start = end
        end += 17
        (_x.index, _x.is_entry, _x.is_exit, _x.is_goal, _x.is_lane_change, _x.is_spot, _x.is_stop, _x.is_perimeter, _x.checkpoint_id, _x.lane_width,) = _struct_H7Bif.unpack(str[start:end])
        val1.is_entry = bool(val1.is_entry)
        val1.is_exit = bool(val1.is_exit)
        val1.is_goal = bool(val1.is_goal)
        val1.is_lane_change = bool(val1.is_lane_change)
        val1.is_spot = bool(val1.is_spot)
        val1.is_stop = bool(val1.is_stop)
        val1.is_perimeter = bool(val1.is_perimeter)
        self.last_order.chkpt.append(val1)
      _x = self
      start = end
      end += 16
      (_x.last_order.min_speed, _x.last_order.max_speed, _x.last_order.replan_num, _x.last_order.next_uturn,) = _struct_2f2i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_8Hi9Bh = struct.Struct("<8Hi9Bh")
_struct_2f2i = struct.Struct("<2f2i")
_struct_H7Bif = struct.Struct("<H7Bif")
_struct_2d = struct.Struct("<2d")
_struct_3I = struct.Struct("<3I")
_struct_3H = struct.Struct("<3H")
_struct_3f = struct.Struct("<3f")
