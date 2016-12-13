# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from skeleton_detection/SkeletonComplete.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import skeleton_detection.msg
import geometry_msgs.msg
import genpy
import std_msgs.msg

class SkeletonComplete(genpy.Message):
  _md5sum = "55e81f9352a265dde8174a2322ddecd9"
  _type = "skeleton_detection/SkeletonComplete"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """std_msgs/Header header
string uuid
time start_time
time end_time
string date
string time
skeleton_detection/skeleton_message[] skeleton_data
skeleton_detection/robot_message[] robot_data
int32 number_of_detections
string map_name
string current_topo_node
geometry_msgs/Point human_map_point

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
MSG: skeleton_detection/skeleton_message
Header header
int32 userID
string uuid
skeleton_detection/joint_message[] joints
time time

================================================================================
MSG: skeleton_detection/joint_message
string name
geometry_msgs/Pose pose
float32 confidence

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: skeleton_detection/robot_message
geometry_msgs/Pose robot_pose
float32 PTU_pan
float32 PTU_tilt
"""
  __slots__ = ['header','uuid','start_time','end_time','date','time','skeleton_data','robot_data','number_of_detections','map_name','current_topo_node','human_map_point']
  _slot_types = ['std_msgs/Header','string','time','time','string','string','skeleton_detection/skeleton_message[]','skeleton_detection/robot_message[]','int32','string','string','geometry_msgs/Point']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,uuid,start_time,end_time,date,time,skeleton_data,robot_data,number_of_detections,map_name,current_topo_node,human_map_point

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SkeletonComplete, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.uuid is None:
        self.uuid = ''
      if self.start_time is None:
        self.start_time = genpy.Time()
      if self.end_time is None:
        self.end_time = genpy.Time()
      if self.date is None:
        self.date = ''
      if self.time is None:
        self.time = ''
      if self.skeleton_data is None:
        self.skeleton_data = []
      if self.robot_data is None:
        self.robot_data = []
      if self.number_of_detections is None:
        self.number_of_detections = 0
      if self.map_name is None:
        self.map_name = ''
      if self.current_topo_node is None:
        self.current_topo_node = ''
      if self.human_map_point is None:
        self.human_map_point = geometry_msgs.msg.Point()
    else:
      self.header = std_msgs.msg.Header()
      self.uuid = ''
      self.start_time = genpy.Time()
      self.end_time = genpy.Time()
      self.date = ''
      self.time = ''
      self.skeleton_data = []
      self.robot_data = []
      self.number_of_detections = 0
      self.map_name = ''
      self.current_topo_node = ''
      self.human_map_point = geometry_msgs.msg.Point()

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
      _x = self.uuid
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4I.pack(_x.start_time.secs, _x.start_time.nsecs, _x.end_time.secs, _x.end_time.nsecs))
      _x = self.date
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.time
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.skeleton_data)
      buff.write(_struct_I.pack(length))
      for val1 in self.skeleton_data:
        _v1 = val1.header
        buff.write(_struct_I.pack(_v1.seq))
        _v2 = _v1.stamp
        _x = _v2
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v1.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_struct_i.pack(val1.userID))
        _x = val1.uuid
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.joints)
        buff.write(_struct_I.pack(length))
        for val2 in val1.joints:
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _v3 = val2.pose
          _v4 = _v3.position
          _x = _v4
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v5 = _v3.orientation
          _x = _v5
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
          buff.write(_struct_f.pack(val2.confidence))
        _v6 = val1.time
        _x = _v6
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
      length = len(self.robot_data)
      buff.write(_struct_I.pack(length))
      for val1 in self.robot_data:
        _v7 = val1.robot_pose
        _v8 = _v7.position
        _x = _v8
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v9 = _v7.orientation
        _x = _v9
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        _x = val1
        buff.write(_struct_2f.pack(_x.PTU_pan, _x.PTU_tilt))
      buff.write(_struct_i.pack(self.number_of_detections))
      _x = self.map_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.current_topo_node
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3d.pack(_x.human_map_point.x, _x.human_map_point.y, _x.human_map_point.z))
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
      if self.start_time is None:
        self.start_time = genpy.Time()
      if self.end_time is None:
        self.end_time = genpy.Time()
      if self.skeleton_data is None:
        self.skeleton_data = None
      if self.robot_data is None:
        self.robot_data = None
      if self.human_map_point is None:
        self.human_map_point = geometry_msgs.msg.Point()
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
      start = end
      end += length
      if python3:
        self.uuid = str[start:end].decode('utf-8')
      else:
        self.uuid = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.start_time.secs, _x.start_time.nsecs, _x.end_time.secs, _x.end_time.nsecs,) = _struct_4I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.date = str[start:end].decode('utf-8')
      else:
        self.date = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.time = str[start:end].decode('utf-8')
      else:
        self.time = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.skeleton_data = []
      for i in range(0, length):
        val1 = skeleton_detection.msg.skeleton_message()
        _v10 = val1.header
        start = end
        end += 4
        (_v10.seq,) = _struct_I.unpack(str[start:end])
        _v11 = _v10.stamp
        _x = _v11
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v10.frame_id = str[start:end].decode('utf-8')
        else:
          _v10.frame_id = str[start:end]
        start = end
        end += 4
        (val1.userID,) = _struct_i.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.uuid = str[start:end].decode('utf-8')
        else:
          val1.uuid = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.joints = []
        for i in range(0, length):
          val2 = skeleton_detection.msg.joint_message()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8')
          else:
            val2.name = str[start:end]
          _v12 = val2.pose
          _v13 = _v12.position
          _x = _v13
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v14 = _v12.orientation
          _x = _v14
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          start = end
          end += 4
          (val2.confidence,) = _struct_f.unpack(str[start:end])
          val1.joints.append(val2)
        _v15 = val1.time
        _x = _v15
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        self.skeleton_data.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.robot_data = []
      for i in range(0, length):
        val1 = skeleton_detection.msg.robot_message()
        _v16 = val1.robot_pose
        _v17 = _v16.position
        _x = _v17
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v18 = _v16.orientation
        _x = _v18
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        _x = val1
        start = end
        end += 8
        (_x.PTU_pan, _x.PTU_tilt,) = _struct_2f.unpack(str[start:end])
        self.robot_data.append(val1)
      start = end
      end += 4
      (self.number_of_detections,) = _struct_i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.map_name = str[start:end].decode('utf-8')
      else:
        self.map_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.current_topo_node = str[start:end].decode('utf-8')
      else:
        self.current_topo_node = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.human_map_point.x, _x.human_map_point.y, _x.human_map_point.z,) = _struct_3d.unpack(str[start:end])
      self.start_time.canon()
      self.end_time.canon()
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
      _x = self.uuid
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4I.pack(_x.start_time.secs, _x.start_time.nsecs, _x.end_time.secs, _x.end_time.nsecs))
      _x = self.date
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.time
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.skeleton_data)
      buff.write(_struct_I.pack(length))
      for val1 in self.skeleton_data:
        _v19 = val1.header
        buff.write(_struct_I.pack(_v19.seq))
        _v20 = _v19.stamp
        _x = _v20
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v19.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_struct_i.pack(val1.userID))
        _x = val1.uuid
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.joints)
        buff.write(_struct_I.pack(length))
        for val2 in val1.joints:
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _v21 = val2.pose
          _v22 = _v21.position
          _x = _v22
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v23 = _v21.orientation
          _x = _v23
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
          buff.write(_struct_f.pack(val2.confidence))
        _v24 = val1.time
        _x = _v24
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
      length = len(self.robot_data)
      buff.write(_struct_I.pack(length))
      for val1 in self.robot_data:
        _v25 = val1.robot_pose
        _v26 = _v25.position
        _x = _v26
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v27 = _v25.orientation
        _x = _v27
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        _x = val1
        buff.write(_struct_2f.pack(_x.PTU_pan, _x.PTU_tilt))
      buff.write(_struct_i.pack(self.number_of_detections))
      _x = self.map_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.current_topo_node
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3d.pack(_x.human_map_point.x, _x.human_map_point.y, _x.human_map_point.z))
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
      if self.start_time is None:
        self.start_time = genpy.Time()
      if self.end_time is None:
        self.end_time = genpy.Time()
      if self.skeleton_data is None:
        self.skeleton_data = None
      if self.robot_data is None:
        self.robot_data = None
      if self.human_map_point is None:
        self.human_map_point = geometry_msgs.msg.Point()
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
      start = end
      end += length
      if python3:
        self.uuid = str[start:end].decode('utf-8')
      else:
        self.uuid = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.start_time.secs, _x.start_time.nsecs, _x.end_time.secs, _x.end_time.nsecs,) = _struct_4I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.date = str[start:end].decode('utf-8')
      else:
        self.date = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.time = str[start:end].decode('utf-8')
      else:
        self.time = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.skeleton_data = []
      for i in range(0, length):
        val1 = skeleton_detection.msg.skeleton_message()
        _v28 = val1.header
        start = end
        end += 4
        (_v28.seq,) = _struct_I.unpack(str[start:end])
        _v29 = _v28.stamp
        _x = _v29
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v28.frame_id = str[start:end].decode('utf-8')
        else:
          _v28.frame_id = str[start:end]
        start = end
        end += 4
        (val1.userID,) = _struct_i.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.uuid = str[start:end].decode('utf-8')
        else:
          val1.uuid = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.joints = []
        for i in range(0, length):
          val2 = skeleton_detection.msg.joint_message()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8')
          else:
            val2.name = str[start:end]
          _v30 = val2.pose
          _v31 = _v30.position
          _x = _v31
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v32 = _v30.orientation
          _x = _v32
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          start = end
          end += 4
          (val2.confidence,) = _struct_f.unpack(str[start:end])
          val1.joints.append(val2)
        _v33 = val1.time
        _x = _v33
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        self.skeleton_data.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.robot_data = []
      for i in range(0, length):
        val1 = skeleton_detection.msg.robot_message()
        _v34 = val1.robot_pose
        _v35 = _v34.position
        _x = _v35
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v36 = _v34.orientation
        _x = _v36
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        _x = val1
        start = end
        end += 8
        (_x.PTU_pan, _x.PTU_tilt,) = _struct_2f.unpack(str[start:end])
        self.robot_data.append(val1)
      start = end
      end += 4
      (self.number_of_detections,) = _struct_i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.map_name = str[start:end].decode('utf-8')
      else:
        self.map_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.current_topo_node = str[start:end].decode('utf-8')
      else:
        self.current_topo_node = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.human_map_point.x, _x.human_map_point.y, _x.human_map_point.z,) = _struct_3d.unpack(str[start:end])
      self.start_time.canon()
      self.end_time.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_f = struct.Struct("<f")
_struct_2f = struct.Struct("<2f")
_struct_i = struct.Struct("<i")
_struct_3I = struct.Struct("<3I")
_struct_4I = struct.Struct("<4I")
_struct_4d = struct.Struct("<4d")
_struct_2I = struct.Struct("<2I")
_struct_3d = struct.Struct("<3d")
