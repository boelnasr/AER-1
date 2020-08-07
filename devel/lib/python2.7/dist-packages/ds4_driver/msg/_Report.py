# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ds4_driver/Report.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class Report(genpy.Message):
  _md5sum = "ec2c37165ced5aec5b7a50d72696b7dc"
  _type = "ds4_driver/Report"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# Raw report from DualShock 4
Header header

# Left: 0, Right: 255
uint8 left_analog_x
# Up: 0, Down: 255
uint8 left_analog_y
uint8 right_analog_x
uint8 right_analog_y

# Released: 0, Pressed: 255
uint8 l2_analog
# Released: 0, Pressed: 255
uint8 r2_analog

# Released: 0, Pressed: 1
bool dpad_up
bool dpad_down
bool dpad_left
bool dpad_right
bool button_cross
bool button_circle
bool button_square
bool button_triangle
bool button_l1
bool button_l2
bool button_l3
bool button_r1
bool button_r2
bool button_r3
bool button_share
bool button_options
bool button_trackpad
bool button_ps

# IMU
int16 lin_acc_x
int16 lin_acc_y
int16 lin_acc_z
int16 ang_vel_x
int16 ang_vel_y
int16 ang_vel_z

# Top-left: (0, 0), Bottom-right: (1919, 942)
uint16 trackpad_touch0_id
uint16 trackpad_touch0_active
uint16 trackpad_touch0_x
uint16 trackpad_touch0_y
uint16 trackpad_touch1_id
uint16 trackpad_touch1_active
uint16 trackpad_touch1_x
uint16 trackpad_touch1_y

uint8 timestamp
# Full: 8, Full (and charging): 11
uint8 battery

# Unused: 0, Plugged: 1
bool plug_usb
bool plug_audio
bool plug_mic

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
string frame_id
"""
  __slots__ = ['header','left_analog_x','left_analog_y','right_analog_x','right_analog_y','l2_analog','r2_analog','dpad_up','dpad_down','dpad_left','dpad_right','button_cross','button_circle','button_square','button_triangle','button_l1','button_l2','button_l3','button_r1','button_r2','button_r3','button_share','button_options','button_trackpad','button_ps','lin_acc_x','lin_acc_y','lin_acc_z','ang_vel_x','ang_vel_y','ang_vel_z','trackpad_touch0_id','trackpad_touch0_active','trackpad_touch0_x','trackpad_touch0_y','trackpad_touch1_id','trackpad_touch1_active','trackpad_touch1_x','trackpad_touch1_y','timestamp','battery','plug_usb','plug_audio','plug_mic']
  _slot_types = ['std_msgs/Header','uint8','uint8','uint8','uint8','uint8','uint8','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','int16','int16','int16','int16','int16','int16','uint16','uint16','uint16','uint16','uint16','uint16','uint16','uint16','uint8','uint8','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,left_analog_x,left_analog_y,right_analog_x,right_analog_y,l2_analog,r2_analog,dpad_up,dpad_down,dpad_left,dpad_right,button_cross,button_circle,button_square,button_triangle,button_l1,button_l2,button_l3,button_r1,button_r2,button_r3,button_share,button_options,button_trackpad,button_ps,lin_acc_x,lin_acc_y,lin_acc_z,ang_vel_x,ang_vel_y,ang_vel_z,trackpad_touch0_id,trackpad_touch0_active,trackpad_touch0_x,trackpad_touch0_y,trackpad_touch1_id,trackpad_touch1_active,trackpad_touch1_x,trackpad_touch1_y,timestamp,battery,plug_usb,plug_audio,plug_mic

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Report, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.left_analog_x is None:
        self.left_analog_x = 0
      if self.left_analog_y is None:
        self.left_analog_y = 0
      if self.right_analog_x is None:
        self.right_analog_x = 0
      if self.right_analog_y is None:
        self.right_analog_y = 0
      if self.l2_analog is None:
        self.l2_analog = 0
      if self.r2_analog is None:
        self.r2_analog = 0
      if self.dpad_up is None:
        self.dpad_up = False
      if self.dpad_down is None:
        self.dpad_down = False
      if self.dpad_left is None:
        self.dpad_left = False
      if self.dpad_right is None:
        self.dpad_right = False
      if self.button_cross is None:
        self.button_cross = False
      if self.button_circle is None:
        self.button_circle = False
      if self.button_square is None:
        self.button_square = False
      if self.button_triangle is None:
        self.button_triangle = False
      if self.button_l1 is None:
        self.button_l1 = False
      if self.button_l2 is None:
        self.button_l2 = False
      if self.button_l3 is None:
        self.button_l3 = False
      if self.button_r1 is None:
        self.button_r1 = False
      if self.button_r2 is None:
        self.button_r2 = False
      if self.button_r3 is None:
        self.button_r3 = False
      if self.button_share is None:
        self.button_share = False
      if self.button_options is None:
        self.button_options = False
      if self.button_trackpad is None:
        self.button_trackpad = False
      if self.button_ps is None:
        self.button_ps = False
      if self.lin_acc_x is None:
        self.lin_acc_x = 0
      if self.lin_acc_y is None:
        self.lin_acc_y = 0
      if self.lin_acc_z is None:
        self.lin_acc_z = 0
      if self.ang_vel_x is None:
        self.ang_vel_x = 0
      if self.ang_vel_y is None:
        self.ang_vel_y = 0
      if self.ang_vel_z is None:
        self.ang_vel_z = 0
      if self.trackpad_touch0_id is None:
        self.trackpad_touch0_id = 0
      if self.trackpad_touch0_active is None:
        self.trackpad_touch0_active = 0
      if self.trackpad_touch0_x is None:
        self.trackpad_touch0_x = 0
      if self.trackpad_touch0_y is None:
        self.trackpad_touch0_y = 0
      if self.trackpad_touch1_id is None:
        self.trackpad_touch1_id = 0
      if self.trackpad_touch1_active is None:
        self.trackpad_touch1_active = 0
      if self.trackpad_touch1_x is None:
        self.trackpad_touch1_x = 0
      if self.trackpad_touch1_y is None:
        self.trackpad_touch1_y = 0
      if self.timestamp is None:
        self.timestamp = 0
      if self.battery is None:
        self.battery = 0
      if self.plug_usb is None:
        self.plug_usb = False
      if self.plug_audio is None:
        self.plug_audio = False
      if self.plug_mic is None:
        self.plug_mic = False
    else:
      self.header = std_msgs.msg.Header()
      self.left_analog_x = 0
      self.left_analog_y = 0
      self.right_analog_x = 0
      self.right_analog_y = 0
      self.l2_analog = 0
      self.r2_analog = 0
      self.dpad_up = False
      self.dpad_down = False
      self.dpad_left = False
      self.dpad_right = False
      self.button_cross = False
      self.button_circle = False
      self.button_square = False
      self.button_triangle = False
      self.button_l1 = False
      self.button_l2 = False
      self.button_l3 = False
      self.button_r1 = False
      self.button_r2 = False
      self.button_r3 = False
      self.button_share = False
      self.button_options = False
      self.button_trackpad = False
      self.button_ps = False
      self.lin_acc_x = 0
      self.lin_acc_y = 0
      self.lin_acc_z = 0
      self.ang_vel_x = 0
      self.ang_vel_y = 0
      self.ang_vel_z = 0
      self.trackpad_touch0_id = 0
      self.trackpad_touch0_active = 0
      self.trackpad_touch0_x = 0
      self.trackpad_touch0_y = 0
      self.trackpad_touch1_id = 0
      self.trackpad_touch1_active = 0
      self.trackpad_touch1_x = 0
      self.trackpad_touch1_y = 0
      self.timestamp = 0
      self.battery = 0
      self.plug_usb = False
      self.plug_audio = False
      self.plug_mic = False

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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_24B6h8H5B().pack(_x.left_analog_x, _x.left_analog_y, _x.right_analog_x, _x.right_analog_y, _x.l2_analog, _x.r2_analog, _x.dpad_up, _x.dpad_down, _x.dpad_left, _x.dpad_right, _x.button_cross, _x.button_circle, _x.button_square, _x.button_triangle, _x.button_l1, _x.button_l2, _x.button_l3, _x.button_r1, _x.button_r2, _x.button_r3, _x.button_share, _x.button_options, _x.button_trackpad, _x.button_ps, _x.lin_acc_x, _x.lin_acc_y, _x.lin_acc_z, _x.ang_vel_x, _x.ang_vel_y, _x.ang_vel_z, _x.trackpad_touch0_id, _x.trackpad_touch0_active, _x.trackpad_touch0_x, _x.trackpad_touch0_y, _x.trackpad_touch1_id, _x.trackpad_touch1_active, _x.trackpad_touch1_x, _x.trackpad_touch1_y, _x.timestamp, _x.battery, _x.plug_usb, _x.plug_audio, _x.plug_mic))
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
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
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
      end += 57
      (_x.left_analog_x, _x.left_analog_y, _x.right_analog_x, _x.right_analog_y, _x.l2_analog, _x.r2_analog, _x.dpad_up, _x.dpad_down, _x.dpad_left, _x.dpad_right, _x.button_cross, _x.button_circle, _x.button_square, _x.button_triangle, _x.button_l1, _x.button_l2, _x.button_l3, _x.button_r1, _x.button_r2, _x.button_r3, _x.button_share, _x.button_options, _x.button_trackpad, _x.button_ps, _x.lin_acc_x, _x.lin_acc_y, _x.lin_acc_z, _x.ang_vel_x, _x.ang_vel_y, _x.ang_vel_z, _x.trackpad_touch0_id, _x.trackpad_touch0_active, _x.trackpad_touch0_x, _x.trackpad_touch0_y, _x.trackpad_touch1_id, _x.trackpad_touch1_active, _x.trackpad_touch1_x, _x.trackpad_touch1_y, _x.timestamp, _x.battery, _x.plug_usb, _x.plug_audio, _x.plug_mic,) = _get_struct_24B6h8H5B().unpack(str[start:end])
      self.dpad_up = bool(self.dpad_up)
      self.dpad_down = bool(self.dpad_down)
      self.dpad_left = bool(self.dpad_left)
      self.dpad_right = bool(self.dpad_right)
      self.button_cross = bool(self.button_cross)
      self.button_circle = bool(self.button_circle)
      self.button_square = bool(self.button_square)
      self.button_triangle = bool(self.button_triangle)
      self.button_l1 = bool(self.button_l1)
      self.button_l2 = bool(self.button_l2)
      self.button_l3 = bool(self.button_l3)
      self.button_r1 = bool(self.button_r1)
      self.button_r2 = bool(self.button_r2)
      self.button_r3 = bool(self.button_r3)
      self.button_share = bool(self.button_share)
      self.button_options = bool(self.button_options)
      self.button_trackpad = bool(self.button_trackpad)
      self.button_ps = bool(self.button_ps)
      self.plug_usb = bool(self.plug_usb)
      self.plug_audio = bool(self.plug_audio)
      self.plug_mic = bool(self.plug_mic)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_24B6h8H5B().pack(_x.left_analog_x, _x.left_analog_y, _x.right_analog_x, _x.right_analog_y, _x.l2_analog, _x.r2_analog, _x.dpad_up, _x.dpad_down, _x.dpad_left, _x.dpad_right, _x.button_cross, _x.button_circle, _x.button_square, _x.button_triangle, _x.button_l1, _x.button_l2, _x.button_l3, _x.button_r1, _x.button_r2, _x.button_r3, _x.button_share, _x.button_options, _x.button_trackpad, _x.button_ps, _x.lin_acc_x, _x.lin_acc_y, _x.lin_acc_z, _x.ang_vel_x, _x.ang_vel_y, _x.ang_vel_z, _x.trackpad_touch0_id, _x.trackpad_touch0_active, _x.trackpad_touch0_x, _x.trackpad_touch0_y, _x.trackpad_touch1_id, _x.trackpad_touch1_active, _x.trackpad_touch1_x, _x.trackpad_touch1_y, _x.timestamp, _x.battery, _x.plug_usb, _x.plug_audio, _x.plug_mic))
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
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
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
      end += 57
      (_x.left_analog_x, _x.left_analog_y, _x.right_analog_x, _x.right_analog_y, _x.l2_analog, _x.r2_analog, _x.dpad_up, _x.dpad_down, _x.dpad_left, _x.dpad_right, _x.button_cross, _x.button_circle, _x.button_square, _x.button_triangle, _x.button_l1, _x.button_l2, _x.button_l3, _x.button_r1, _x.button_r2, _x.button_r3, _x.button_share, _x.button_options, _x.button_trackpad, _x.button_ps, _x.lin_acc_x, _x.lin_acc_y, _x.lin_acc_z, _x.ang_vel_x, _x.ang_vel_y, _x.ang_vel_z, _x.trackpad_touch0_id, _x.trackpad_touch0_active, _x.trackpad_touch0_x, _x.trackpad_touch0_y, _x.trackpad_touch1_id, _x.trackpad_touch1_active, _x.trackpad_touch1_x, _x.trackpad_touch1_y, _x.timestamp, _x.battery, _x.plug_usb, _x.plug_audio, _x.plug_mic,) = _get_struct_24B6h8H5B().unpack(str[start:end])
      self.dpad_up = bool(self.dpad_up)
      self.dpad_down = bool(self.dpad_down)
      self.dpad_left = bool(self.dpad_left)
      self.dpad_right = bool(self.dpad_right)
      self.button_cross = bool(self.button_cross)
      self.button_circle = bool(self.button_circle)
      self.button_square = bool(self.button_square)
      self.button_triangle = bool(self.button_triangle)
      self.button_l1 = bool(self.button_l1)
      self.button_l2 = bool(self.button_l2)
      self.button_l3 = bool(self.button_l3)
      self.button_r1 = bool(self.button_r1)
      self.button_r2 = bool(self.button_r2)
      self.button_r3 = bool(self.button_r3)
      self.button_share = bool(self.button_share)
      self.button_options = bool(self.button_options)
      self.button_trackpad = bool(self.button_trackpad)
      self.button_ps = bool(self.button_ps)
      self.plug_usb = bool(self.plug_usb)
      self.plug_audio = bool(self.plug_audio)
      self.plug_mic = bool(self.plug_mic)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_24B6h8H5B = None
def _get_struct_24B6h8H5B():
    global _struct_24B6h8H5B
    if _struct_24B6h8H5B is None:
        _struct_24B6h8H5B = struct.Struct("<24B6h8H5B")
    return _struct_24B6h8H5B
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
