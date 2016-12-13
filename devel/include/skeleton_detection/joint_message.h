// Generated by gencpp from file skeleton_detection/joint_message.msg
// DO NOT EDIT!


#ifndef SKELETON_DETECTION_MESSAGE_JOINT_MESSAGE_H
#define SKELETON_DETECTION_MESSAGE_JOINT_MESSAGE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Pose.h>

namespace skeleton_detection
{
template <class ContainerAllocator>
struct joint_message_
{
  typedef joint_message_<ContainerAllocator> Type;

  joint_message_()
    : name()
    , pose()
    , confidence(0.0)  {
    }
  joint_message_(const ContainerAllocator& _alloc)
    : name(_alloc)
    , pose(_alloc)
    , confidence(0.0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _name_type;
  _name_type name;

   typedef  ::geometry_msgs::Pose_<ContainerAllocator>  _pose_type;
  _pose_type pose;

   typedef float _confidence_type;
  _confidence_type confidence;




  typedef boost::shared_ptr< ::skeleton_detection::joint_message_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::skeleton_detection::joint_message_<ContainerAllocator> const> ConstPtr;

}; // struct joint_message_

typedef ::skeleton_detection::joint_message_<std::allocator<void> > joint_message;

typedef boost::shared_ptr< ::skeleton_detection::joint_message > joint_messagePtr;
typedef boost::shared_ptr< ::skeleton_detection::joint_message const> joint_messageConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::skeleton_detection::joint_message_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::skeleton_detection::joint_message_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::skeleton_detection::joint_message_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::skeleton_detection::joint_message_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::skeleton_detection::joint_message_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::skeleton_detection::joint_message_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::skeleton_detection::joint_message_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::skeleton_detection::joint_message_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::skeleton_detection::joint_message_<ContainerAllocator> >
{
  static const char* value()
  {
    return "7de55f1f1b693325f4b111ca4e88f2a6";
  }

  static const char* value(const ::skeleton_detection::joint_message_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x7de55f1f1b693325ULL;
  static const uint64_t static_value2 = 0xf4b111ca4e88f2a6ULL;
};

template<class ContainerAllocator>
struct DataType< ::skeleton_detection::joint_message_<ContainerAllocator> >
{
  static const char* value()
  {
    return "skeleton_detection/joint_message";
  }

  static const char* value(const ::skeleton_detection::joint_message_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::skeleton_detection::joint_message_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string name\n\
geometry_msgs/Pose pose\n\
float32 confidence\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Pose\n\
# A representation of pose in free space, composed of postion and orientation. \n\
Point position\n\
Quaternion orientation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
";
  }

  static const char* value(const ::skeleton_detection::joint_message_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::skeleton_detection::joint_message_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.name);
      stream.next(m.pose);
      stream.next(m.confidence);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct joint_message_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::skeleton_detection::joint_message_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::skeleton_detection::joint_message_<ContainerAllocator>& v)
  {
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.name);
    s << indent << "pose: ";
    s << std::endl;
    Printer< ::geometry_msgs::Pose_<ContainerAllocator> >::stream(s, indent + "  ", v.pose);
    s << indent << "confidence: ";
    Printer<float>::stream(s, indent + "  ", v.confidence);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SKELETON_DETECTION_MESSAGE_JOINT_MESSAGE_H
