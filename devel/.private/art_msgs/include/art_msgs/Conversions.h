// Generated by gencpp from file art_msgs/Conversions.msg
// DO NOT EDIT!


#ifndef ART_MSGS_MESSAGE_CONVERSIONS_H
#define ART_MSGS_MESSAGE_CONVERSIONS_H


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
struct Conversions_
{
  typedef Conversions_<ContainerAllocator> Type;

  Conversions_()
    {
    }
  Conversions_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }




    static const double CM_PER_INCH;
     static const double CM_PER_METER;
     static const double INCHES_PER_FOOT;
     static const double METERS_PER_FOOT;
     static const double METERS_PER_MILE;
     static const double MMETERS_PER_KM;
     static const double MMETERS_PER_MILE;
     enum { MINUTES_PER_HOUR = 60 };
     enum { SECONDS_PER_MINUTE = 60 };
     enum { SECONDS_PER_HOUR = 3600 };
 

  typedef boost::shared_ptr< ::art_msgs::Conversions_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::art_msgs::Conversions_<ContainerAllocator> const> ConstPtr;

}; // struct Conversions_

typedef ::art_msgs::Conversions_<std::allocator<void> > Conversions;

typedef boost::shared_ptr< ::art_msgs::Conversions > ConversionsPtr;
typedef boost::shared_ptr< ::art_msgs::Conversions const> ConversionsConstPtr;

// constants requiring out of line definition

   
   template<typename ContainerAllocator> const double
      Conversions_<ContainerAllocator>::CM_PER_INCH =
        
          2.54
        
        ;
   

   
   template<typename ContainerAllocator> const double
      Conversions_<ContainerAllocator>::CM_PER_METER =
        
          100.0
        
        ;
   

   
   template<typename ContainerAllocator> const double
      Conversions_<ContainerAllocator>::INCHES_PER_FOOT =
        
          12.0
        
        ;
   

   
   template<typename ContainerAllocator> const double
      Conversions_<ContainerAllocator>::METERS_PER_FOOT =
        
          0.3048
        
        ;
   

   
   template<typename ContainerAllocator> const double
      Conversions_<ContainerAllocator>::METERS_PER_MILE =
        
          1609.344
        
        ;
   

   
   template<typename ContainerAllocator> const double
      Conversions_<ContainerAllocator>::MMETERS_PER_KM =
        
          1000000.0
        
        ;
   

   
   template<typename ContainerAllocator> const double
      Conversions_<ContainerAllocator>::MMETERS_PER_MILE =
        
          1609344.0
        
        ;
   

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::art_msgs::Conversions_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::art_msgs::Conversions_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::art_msgs::Conversions_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::art_msgs::Conversions_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::art_msgs::Conversions_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::art_msgs::Conversions_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::art_msgs::Conversions_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::art_msgs::Conversions_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::art_msgs::Conversions_<ContainerAllocator> >
{
  static const char* value()
  {
    return "44629a726979d07e4fc2da05a3fca804";
  }

  static const char* value(const ::art_msgs::Conversions_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x44629a726979d07eULL;
  static const uint64_t static_value2 = 0x4fc2da05a3fca804ULL;
};

template<class ContainerAllocator>
struct DataType< ::art_msgs::Conversions_<ContainerAllocator> >
{
  static const char* value()
  {
    return "art_msgs/Conversions";
  }

  static const char* value(const ::art_msgs::Conversions_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::art_msgs::Conversions_<ContainerAllocator> >
{
  static const char* value()
  {
    return "#  Units conversion constants\n\
#\n\
#  Copyright (C) 2007, 2009 Austin Robot Technology                    \n\
#  License: Modified BSD Software License Agreement\n\
\n\
#  $Id$\n\
\n\
# Unit conversion constants:\n\
\n\
float64 CM_PER_INCH = 2.54\n\
float64 CM_PER_METER = 100.0\n\
float64 INCHES_PER_FOOT = 12.0\n\
float64 METERS_PER_FOOT = 0.3048\n\
float64 METERS_PER_MILE = 1609.344\n\
float64 MMETERS_PER_KM = 1000000.0\n\
float64 MMETERS_PER_MILE = 1609344.0\n\
\n\
int64 MINUTES_PER_HOUR = 60\n\
int64 SECONDS_PER_MINUTE = 60\n\
int64 SECONDS_PER_HOUR = 3600\n\
";
  }

  static const char* value(const ::art_msgs::Conversions_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::art_msgs::Conversions_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Conversions_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::art_msgs::Conversions_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::art_msgs::Conversions_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // ART_MSGS_MESSAGE_CONVERSIONS_H
