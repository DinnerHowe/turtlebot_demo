// Generated by gencpp from file skeleton_detection/skeleton_detection_state.msg
// DO NOT EDIT!


#ifndef SKELETON_DETECTION_MESSAGE_SKELETON_DETECTION_STATE_H
#define SKELETON_DETECTION_MESSAGE_SKELETON_DETECTION_STATE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace skeleton_detection
{
template <class ContainerAllocator>
struct skeleton_detection_state_
{
  typedef skeleton_detection_state_<ContainerAllocator> Type;

  skeleton_detection_state_()
    : userID(0)
    , uuid()
    , timepoint(0)
    , message()  {
    }
  skeleton_detection_state_(const ContainerAllocator& _alloc)
    : userID(0)
    , uuid(_alloc)
    , timepoint(0)
    , message(_alloc)  {
  (void)_alloc;
    }



   typedef int32_t _userID_type;
  _userID_type userID;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _uuid_type;
  _uuid_type uuid;

   typedef int32_t _timepoint_type;
  _timepoint_type timepoint;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _message_type;
  _message_type message;




  typedef boost::shared_ptr< ::skeleton_detection::skeleton_detection_state_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::skeleton_detection::skeleton_detection_state_<ContainerAllocator> const> ConstPtr;

}; // struct skeleton_detection_state_

typedef ::skeleton_detection::skeleton_detection_state_<std::allocator<void> > skeleton_detection_state;

typedef boost::shared_ptr< ::skeleton_detection::skeleton_detection_state > skeleton_detection_statePtr;
typedef boost::shared_ptr< ::skeleton_detection::skeleton_detection_state const> skeleton_detection_stateConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::skeleton_detection::skeleton_detection_state_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::skeleton_detection::skeleton_detection_state_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace skeleton_detection

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'skeleton_detection': ['/home/howe/turtlebot_demo/src/skeleton_detection/skeleton_detection/msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::skeleton_detection::skeleton_detection_state_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::skeleton_detection::skeleton_detection_state_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::skeleton_detection::skeleton_detection_state_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::skeleton_detection::skeleton_detection_state_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::skeleton_detection::skeleton_detection_state_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::skeleton_detection::skeleton_detection_state_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::skeleton_detection::skeleton_detection_state_<ContainerAllocator> >
{
  static const char* value()
  {
    return "9b2faf0f5d20df98d0fee14cd4de7fe9";
  }

  static const char* value(const ::skeleton_detection::skeleton_detection_state_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x9b2faf0f5d20df98ULL;
  static const uint64_t static_value2 = 0xd0fee14cd4de7fe9ULL;
};

template<class ContainerAllocator>
struct DataType< ::skeleton_detection::skeleton_detection_state_<ContainerAllocator> >
{
  static const char* value()
  {
    return "skeleton_detection/skeleton_detection_state";
  }

  static const char* value(const ::skeleton_detection::skeleton_detection_state_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::skeleton_detection::skeleton_detection_state_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 userID\n\
string uuid\n\
int32 timepoint\n\
string message\n\
\n\
";
  }

  static const char* value(const ::skeleton_detection::skeleton_detection_state_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::skeleton_detection::skeleton_detection_state_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.userID);
      stream.next(m.uuid);
      stream.next(m.timepoint);
      stream.next(m.message);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct skeleton_detection_state_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::skeleton_detection::skeleton_detection_state_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::skeleton_detection::skeleton_detection_state_<ContainerAllocator>& v)
  {
    s << indent << "userID: ";
    Printer<int32_t>::stream(s, indent + "  ", v.userID);
    s << indent << "uuid: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.uuid);
    s << indent << "timepoint: ";
    Printer<int32_t>::stream(s, indent + "  ", v.timepoint);
    s << indent << "message: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.message);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SKELETON_DETECTION_MESSAGE_SKELETON_DETECTION_STATE_H
