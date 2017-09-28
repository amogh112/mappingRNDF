// Generated by gencpp from file art_msgs/SteeringDiagnostics.msg
// DO NOT EDIT!


#ifndef ART_MSGS_MESSAGE_STEERINGDIAGNOSTICS_H
#define ART_MSGS_MESSAGE_STEERINGDIAGNOSTICS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace art_msgs
{
template <class ContainerAllocator>
struct SteeringDiagnostics_
{
  typedef SteeringDiagnostics_<ContainerAllocator> Type;

  SteeringDiagnostics_()
    : header()
    , encoder(0)
    , last_request(0)
    , center_ticks(0)
    , status_word(0)  {
    }
  SteeringDiagnostics_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , encoder(0)
    , last_request(0)
    , center_ticks(0)
    , status_word(0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef int32_t _encoder_type;
  _encoder_type encoder;

   typedef int32_t _last_request_type;
  _last_request_type last_request;

   typedef int32_t _center_ticks_type;
  _center_ticks_type center_ticks;

   typedef uint16_t _status_word_type;
  _status_word_type status_word;




  typedef boost::shared_ptr< ::art_msgs::SteeringDiagnostics_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::art_msgs::SteeringDiagnostics_<ContainerAllocator> const> ConstPtr;

}; // struct SteeringDiagnostics_

typedef ::art_msgs::SteeringDiagnostics_<std::allocator<void> > SteeringDiagnostics;

typedef boost::shared_ptr< ::art_msgs::SteeringDiagnostics > SteeringDiagnosticsPtr;
typedef boost::shared_ptr< ::art_msgs::SteeringDiagnostics const> SteeringDiagnosticsConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::art_msgs::SteeringDiagnostics_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::art_msgs::SteeringDiagnostics_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::art_msgs::SteeringDiagnostics_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::art_msgs::SteeringDiagnostics_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::art_msgs::SteeringDiagnostics_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::art_msgs::SteeringDiagnostics_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::art_msgs::SteeringDiagnostics_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::art_msgs::SteeringDiagnostics_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::art_msgs::SteeringDiagnostics_<ContainerAllocator> >
{
  static const char* value()
  {
    return "5dbe64bbef789e785f8333e897956d94";
  }

  static const char* value(const ::art_msgs::SteeringDiagnostics_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x5dbe64bbef789e78ULL;
  static const uint64_t static_value2 = 0x5f8333e897956d94ULL;
};

template<class ContainerAllocator>
struct DataType< ::art_msgs::SteeringDiagnostics_<ContainerAllocator> >
{
  static const char* value()
  {
    return "art_msgs/SteeringDiagnostics";
  }

  static const char* value(const ::art_msgs::SteeringDiagnostics_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::art_msgs::SteeringDiagnostics_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ART steering controller diagnostics message\n\
\n\
# This message contains data not needed for normal operation of the\n\
# device, but useful for diagnosing problems with it.\n\
\n\
# $Id$\n\
\n\
Header  header\n\
\n\
int32 encoder                   # current reported encoder value\n\
int32 last_request              # last requested encoder value\n\
int32 center_ticks              # initial center encoder value\n\
uint16 status_word		# current internal status\n\
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
";
  }

  static const char* value(const ::art_msgs::SteeringDiagnostics_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::art_msgs::SteeringDiagnostics_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.encoder);
      stream.next(m.last_request);
      stream.next(m.center_ticks);
      stream.next(m.status_word);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SteeringDiagnostics_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::art_msgs::SteeringDiagnostics_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::art_msgs::SteeringDiagnostics_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "encoder: ";
    Printer<int32_t>::stream(s, indent + "  ", v.encoder);
    s << indent << "last_request: ";
    Printer<int32_t>::stream(s, indent + "  ", v.last_request);
    s << indent << "center_ticks: ";
    Printer<int32_t>::stream(s, indent + "  ", v.center_ticks);
    s << indent << "status_word: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.status_word);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ART_MSGS_MESSAGE_STEERINGDIAGNOSTICS_H