// Generated by gencpp from file art_msgs/NavigatorState.msg
// DO NOT EDIT!


#ifndef ART_MSGS_MESSAGE_NAVIGATORSTATE_H
#define ART_MSGS_MESSAGE_NAVIGATORSTATE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <art_msgs/EstopState.h>
#include <art_msgs/RoadState.h>
#include <art_msgs/MapID.h>
#include <art_msgs/MapID.h>
#include <art_msgs/Order.h>

namespace art_msgs
{
template <class ContainerAllocator>
struct NavigatorState_
{
  typedef NavigatorState_<ContainerAllocator> Type;

  NavigatorState_()
    : header()
    , estop()
    , road()
    , last_waypt()
    , replan_waypt()
    , cur_poly(0)
    , alarm(false)
    , flasher(false)
    , lane_blocked(false)
    , road_blocked(false)
    , reverse(false)
    , signal_left(false)
    , signal_right(false)
    , stopped(false)
    , have_zones(false)
    , last_order()  {
    }
  NavigatorState_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , estop(_alloc)
    , road(_alloc)
    , last_waypt(_alloc)
    , replan_waypt(_alloc)
    , cur_poly(0)
    , alarm(false)
    , flasher(false)
    , lane_blocked(false)
    , road_blocked(false)
    , reverse(false)
    , signal_left(false)
    , signal_right(false)
    , stopped(false)
    , have_zones(false)
    , last_order(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef  ::art_msgs::EstopState_<ContainerAllocator>  _estop_type;
  _estop_type estop;

   typedef  ::art_msgs::RoadState_<ContainerAllocator>  _road_type;
  _road_type road;

   typedef  ::art_msgs::MapID_<ContainerAllocator>  _last_waypt_type;
  _last_waypt_type last_waypt;

   typedef  ::art_msgs::MapID_<ContainerAllocator>  _replan_waypt_type;
  _replan_waypt_type replan_waypt;

   typedef int32_t _cur_poly_type;
  _cur_poly_type cur_poly;

   typedef uint8_t _alarm_type;
  _alarm_type alarm;

   typedef uint8_t _flasher_type;
  _flasher_type flasher;

   typedef uint8_t _lane_blocked_type;
  _lane_blocked_type lane_blocked;

   typedef uint8_t _road_blocked_type;
  _road_blocked_type road_blocked;

   typedef uint8_t _reverse_type;
  _reverse_type reverse;

   typedef uint8_t _signal_left_type;
  _signal_left_type signal_left;

   typedef uint8_t _signal_right_type;
  _signal_right_type signal_right;

   typedef uint8_t _stopped_type;
  _stopped_type stopped;

   typedef uint8_t _have_zones_type;
  _have_zones_type have_zones;

   typedef  ::art_msgs::Order_<ContainerAllocator>  _last_order_type;
  _last_order_type last_order;




  typedef boost::shared_ptr< ::art_msgs::NavigatorState_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::art_msgs::NavigatorState_<ContainerAllocator> const> ConstPtr;

}; // struct NavigatorState_

typedef ::art_msgs::NavigatorState_<std::allocator<void> > NavigatorState;

typedef boost::shared_ptr< ::art_msgs::NavigatorState > NavigatorStatePtr;
typedef boost::shared_ptr< ::art_msgs::NavigatorState const> NavigatorStateConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::art_msgs::NavigatorState_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::art_msgs::NavigatorState_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace art_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'nav_msgs': ['/opt/ros/indigo/share/nav_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/indigo/share/actionlib_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/indigo/share/sensor_msgs/cmake/../msg'], 'art_msgs': ['/home/amogh/rosws2/src/art_msgs/msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::art_msgs::NavigatorState_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::art_msgs::NavigatorState_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::art_msgs::NavigatorState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::art_msgs::NavigatorState_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::art_msgs::NavigatorState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::art_msgs::NavigatorState_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::art_msgs::NavigatorState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c40e5f1fdc1b82b80af736960035d5c8";
  }

  static const char* value(const ::art_msgs::NavigatorState_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc40e5f1fdc1b82b8ULL;
  static const uint64_t static_value2 = 0x0af736960035d5c8ULL;
};

template<class ContainerAllocator>
struct DataType< ::art_msgs::NavigatorState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "art_msgs/NavigatorState";
  }

  static const char* value(const ::art_msgs::NavigatorState_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::art_msgs::NavigatorState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# navigator state message\n\
# $Id$\n\
\n\
Header header\n\
\n\
EstopState estop\n\
RoadState road\n\
\n\
art_msgs/MapID last_waypt		# last way-point reached\n\
art_msgs/MapID replan_waypt		# next way-point for replan\n\
\n\
int32 cur_poly                          # current polygon, -1 if none\n\
\n\
# status flags\n\
bool alarm\n\
bool flasher\n\
bool lane_blocked\n\
bool road_blocked\n\
bool reverse\n\
bool signal_left\n\
bool signal_right\n\
bool stopped\n\
bool have_zones\n\
\n\
Order last_order			# last commander order received\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: art_msgs/EstopState\n\
# Navigator E-stop state values\n\
# $Id$\n\
\n\
uint16 Pause    = 0			# E-stop pause (initial state)\n\
uint16 Run      = 1			# E-stop run enabled\n\
uint16 Done     = 2			# mission finished (disabled)\n\
uint16 Suspend  = 3			# suspend autonomous operation\n\
uint16 N_states = 4\n\
\n\
uint16 state\n\
\n\
================================================================================\n\
MSG: art_msgs/RoadState\n\
# Navigator Road state values\n\
# $Id$\n\
\n\
uint16 Init      = 0\n\
uint16 Block     = 1\n\
uint16 Evade     = 2\n\
uint16 Follow    = 3\n\
uint16 Pass      = 4\n\
uint16 Uturn     = 5\n\
uint16 WaitCross = 6\n\
uint16 WaitLane  = 7\n\
uint16 WaitPass  = 8\n\
uint16 WaitStop  = 9\n\
uint16 Zone      = 10\n\
uint16 N_states  = 11\n\
\n\
uint16 state\n\
\n\
================================================================================\n\
MSG: art_msgs/MapID\n\
# Road map identifier for segments, lanes and way-points.\n\
# $Id$\n\
\n\
uint16 NULL_ID = 65535\n\
\n\
uint16 seg      # segment ID\n\
uint16 lane     # lane ID\n\
uint16 pt       # way-point ID\n\
\n\
================================================================================\n\
MSG: art_msgs/Order\n\
# commander order for the navigator\n\
# $Id$\n\
\n\
uint32 N_WAYPTS = 5     		# number of way-points in order\n\
uint32 N_CHKPTS = 2             	# number of checkpoints in order\n\
\n\
Behavior behavior			# requested behavior\n\
art_msgs/WayPoint[5] waypt       	# way-point array\n\
art_msgs/WayPoint[2] chkpt       	# next two goal checkpoints\n\
float32 min_speed			# in meters/sec\n\
float32 max_speed\n\
int32 replan_num\n\
int32 next_uturn         		# Uturn between [1] and [2]\n\
\n\
================================================================================\n\
MSG: art_msgs/Behavior\n\
# ART Navigator behaviors (lower numbers have higher priority)\n\
# $Id$\n\
\n\
# enumerated behavior values\n\
int16 Abort       = 0\n\
int16 Quit        = 1\n\
int16 Pause       = 2\n\
int16 Run         = 3\n\
int16 Suspend     = 4\n\
int16 Initialize  = 5\n\
int16 Go          = 6\n\
int16 NONE        = 7\n\
int16 N_behaviors = 8\n\
\n\
int16 value\n\
\n\
================================================================================\n\
MSG: art_msgs/WayPoint\n\
# Way-point attributes\n\
# $Id$\n\
\n\
float64 latitude			# latitude in degrees\n\
float64 longitude			# longitude in degrees\n\
geometry_msgs/Point32 mapxy		# MapXY position\n\
MapID id				# way-point ID\n\
uint16 index    			# parser index of waypoint\n\
\n\
# way-point flags\n\
bool is_entry                           # lane or zone exit point\n\
bool is_exit				# lane or zone entry point\n\
bool is_goal				# this is a goal checkpoint\n\
bool is_lane_change			# change lanes after here\n\
bool is_spot				# parking spot\n\
bool is_stop				# stop line here\n\
bool is_perimeter			# zone perimeter point\n\
int32 checkpoint_id			# checkpoint ID or zero\n\
float32 lane_width\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point32\n\
# This contains the position of a point in free space(with 32 bits of precision).\n\
# It is recommeded to use Point wherever possible instead of Point32.  \n\
# \n\
# This recommendation is to promote interoperability.  \n\
#\n\
# This message is designed to take up less space when sending\n\
# lots of points at once, as in the case of a PointCloud.  \n\
\n\
float32 x\n\
float32 y\n\
float32 z\n\
";
  }

  static const char* value(const ::art_msgs::NavigatorState_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::art_msgs::NavigatorState_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.estop);
      stream.next(m.road);
      stream.next(m.last_waypt);
      stream.next(m.replan_waypt);
      stream.next(m.cur_poly);
      stream.next(m.alarm);
      stream.next(m.flasher);
      stream.next(m.lane_blocked);
      stream.next(m.road_blocked);
      stream.next(m.reverse);
      stream.next(m.signal_left);
      stream.next(m.signal_right);
      stream.next(m.stopped);
      stream.next(m.have_zones);
      stream.next(m.last_order);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct NavigatorState_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::art_msgs::NavigatorState_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::art_msgs::NavigatorState_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "estop: ";
    s << std::endl;
    Printer< ::art_msgs::EstopState_<ContainerAllocator> >::stream(s, indent + "  ", v.estop);
    s << indent << "road: ";
    s << std::endl;
    Printer< ::art_msgs::RoadState_<ContainerAllocator> >::stream(s, indent + "  ", v.road);
    s << indent << "last_waypt: ";
    s << std::endl;
    Printer< ::art_msgs::MapID_<ContainerAllocator> >::stream(s, indent + "  ", v.last_waypt);
    s << indent << "replan_waypt: ";
    s << std::endl;
    Printer< ::art_msgs::MapID_<ContainerAllocator> >::stream(s, indent + "  ", v.replan_waypt);
    s << indent << "cur_poly: ";
    Printer<int32_t>::stream(s, indent + "  ", v.cur_poly);
    s << indent << "alarm: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.alarm);
    s << indent << "flasher: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.flasher);
    s << indent << "lane_blocked: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.lane_blocked);
    s << indent << "road_blocked: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.road_blocked);
    s << indent << "reverse: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.reverse);
    s << indent << "signal_left: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.signal_left);
    s << indent << "signal_right: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.signal_right);
    s << indent << "stopped: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.stopped);
    s << indent << "have_zones: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.have_zones);
    s << indent << "last_order: ";
    s << std::endl;
    Printer< ::art_msgs::Order_<ContainerAllocator> >::stream(s, indent + "  ", v.last_order);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ART_MSGS_MESSAGE_NAVIGATORSTATE_H