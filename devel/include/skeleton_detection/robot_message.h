// Generated by gencpp from file skeleton_detection/robot_message.msg
// DO NOT EDIT!


#ifndef SKELETON_DETECTION_MESSAGE_ROBOT_MESSAGE_H
#define SKELETON_DETECTION_MESSAGE_ROBOT_MESSAGE_H


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
struct robot_message_
{
  typedef robot_message_<ContainerAllocator> Type;

  robot_message_()
    : robot_pose()
    , PTU_pan(0.0)
    , PTU_tilt(0.0)  {
    }
  robot_message_(const ContainerAllocator& _alloc)
    : robot_pose(_alloc)
    , PTU_pan(0.0)
    , PTU_tilt(0.0)  {
  (void)_alloc;
    }



   typedef  ::geometry_msgs::Pose_<ContainerAllocator>  _robot_pose_type;
  _robot_pose_type robot_pose;

   typedef float _PTU_pan_type;
  _PTU_pan_type PTU_pan;

   typedef float _PTU_tilt_type;
  _PTU_tilt_type PTU_tilt;




  typedef boost::shared_ptr< ::skeleton_detection::robot_message_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::skeleton_detection::robot_message_<ContainerAllocator> const> ConstPtr;

}; // struct robot_message_

typedef ::skeleton_detection::robot_message_<std::allocator<void> > robot_message;

typedef boost::shared_ptr< ::skeleton_detection::robot_message > robot_messagePtr;
typedef boost::shared_ptr< ::skeleton_detection::robot_message const> robot_messageConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::skeleton_detection::robot_message_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::skeleton_detection::robot_message_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace skeleton_detection

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'skeleton_detection': ['/home/howe/turtlebot_demo/src/skeleton_detection/skeleton_detection/msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::skeleton_detection::robot_message_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::skeleton_detection::robot_message_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::skeleton_detection::robot_message_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::skeleton_detection::robot_message_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::skeleton_detection::robot_message_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::skeleton_detection::robot_message_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::skeleton_detection::robot_message_<ContainerAllocator> >
{
  static const char* value()
  {
    return "5b4c6123fc326f54f2a02dd17fb35757";
  }

  static const char* value(const ::skeleton_detection::robot_message_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x5b4c6123fc326f54ULL;
  static const uint64_t static_value2 = 0xf2a02dd17fb35757ULL;
};

template<class ContainerAllocator>
struct DataType< ::skeleton_detection::robot_message_<ContainerAllocator> >
{
  static const char* value()
  {
    return "skeleton_detection/robot_message";
  }

  static const char* value(const ::skeleton_detection::robot_message_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::skeleton_detection::robot_message_<ContainerAllocator> >
{
  static const char* value()
  {
    return "geometry_msgs/Pose robot_pose\n\
float32 PTU_pan\n\
float32 PTU_tilt\n\
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

  static const char* value(const ::skeleton_detection::robot_message_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::skeleton_detection::robot_message_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.robot_pose);
      stream.next(m.PTU_pan);
      stream.next(m.PTU_tilt);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct robot_message_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::skeleton_detection::robot_message_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::skeleton_detection::robot_message_<ContainerAllocator>& v)
  {
    s << indent << "robot_pose: ";
    s << std::endl;
    Printer< ::geometry_msgs::Pose_<ContainerAllocator> >::stream(s, indent + "  ", v.robot_pose);
    s << indent << "PTU_pan: ";
    Printer<float>::stream(s, indent + "  ", v.PTU_pan);
    s << indent << "PTU_tilt: ";
    Printer<float>::stream(s, indent + "  ", v.PTU_tilt);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SKELETON_DETECTION_MESSAGE_ROBOT_MESSAGE_H
