// Generated by gencpp from file art_msgs/EstopState.msg
// DO NOT EDIT!


#ifndef ART_MSGS_MESSAGE_ESTOPSTATE_H
#define ART_MSGS_MESSAGE_ESTOPSTATE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace art_msgs
{
template <class ContainerAllocator>
struct EstopState_
{
  typedef EstopState_<ContainerAllocator> Type;

  EstopState_()
    : state(0)  {
    }
  EstopState_(const ContainerAllocator& _alloc)
    : state(0)  {
  (void)_alloc;
    }



   typedef uint16_t _state_type;
  _state_type state;


    enum { Pause = 0u };
     enum { Run = 1u };
     enum { Done = 2u };
     enum { Suspend = 3u };
     enum { N_states = 4u };
 

  typedef boost::shared_ptr< ::art_msgs::EstopState_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::art_msgs::EstopState_<ContainerAllocator> const> ConstPtr;

}; // struct EstopState_

typedef ::art_msgs::EstopState_<std::allocator<void> > EstopState;

typedef boost::shared_ptr< ::art_msgs::EstopState > EstopStatePtr;
typedef boost::shared_ptr< ::art_msgs::EstopState const> EstopStateConstPtr;

// constants requiring out of line definition

   

   

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::art_msgs::EstopState_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::art_msgs::EstopState_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace art_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'nav_msgs': ['/opt/ros/indigo/share/nav_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/indigo/share/actionlib_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/indigo/share/sensor_msgs/cmake/../msg'], 'art_msgs': ['/home/amogh/rosws2/src/art_msgs/msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::art_msgs::EstopState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::art_msgs::EstopState_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::art_msgs::EstopState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::art_msgs::EstopState_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::art_msgs::EstopState_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::art_msgs::EstopState_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::art_msgs::EstopState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "195d9329d308e6ca2b9145be58b92e7e";
  }

  static const char* value(const ::art_msgs::EstopState_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x195d9329d308e6caULL;
  static const uint64_t static_value2 = 0x2b9145be58b92e7eULL;
};

template<class ContainerAllocator>
struct DataType< ::art_msgs::EstopState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "art_msgs/EstopState";
  }

  static const char* value(const ::art_msgs::EstopState_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::art_msgs::EstopState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Navigator E-stop state values\n\
# $Id$\n\
\n\
uint16 Pause    = 0			# E-stop pause (initial state)\n\
uint16 Run      = 1			# E-stop run enabled\n\
uint16 Done     = 2			# mission finished (disabled)\n\
uint16 Suspend  = 3			# suspend autonomous operation\n\
uint16 N_states = 4\n\
\n\
uint16 state\n\
";
  }

  static const char* value(const ::art_msgs::EstopState_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::art_msgs::EstopState_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.state);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct EstopState_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::art_msgs::EstopState_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::art_msgs::EstopState_<ContainerAllocator>& v)
  {
    s << indent << "state: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.state);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ART_MSGS_MESSAGE_ESTOPSTATE_H
