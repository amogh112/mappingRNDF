; Auto-generated. Do not edit!


(cl:in-package art_msgs-msg)


;//! \htmlinclude ThrottleCommand.msg.html

(cl:defclass <ThrottleCommand> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (request
    :reader request
    :initarg :request
    :type cl:integer
    :initform 0)
   (position
    :reader position
    :initarg :position
    :type cl:float
    :initform 0.0))
)

(cl:defclass ThrottleCommand (<ThrottleCommand>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ThrottleCommand>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ThrottleCommand)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name art_msgs-msg:<ThrottleCommand> is deprecated: use art_msgs-msg:ThrottleCommand instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ThrottleCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader art_msgs-msg:header-val is deprecated.  Use art_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'request-val :lambda-list '(m))
(cl:defmethod request-val ((m <ThrottleCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader art_msgs-msg:request-val is deprecated.  Use art_msgs-msg:request instead.")
  (request m))

(cl:ensure-generic-function 'position-val :lambda-list '(m))
(cl:defmethod position-val ((m <ThrottleCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader art_msgs-msg:position-val is deprecated.  Use art_msgs-msg:position instead.")
  (position m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<ThrottleCommand>)))
    "Constants for message type '<ThrottleCommand>"
  '((:ABSOLUTE . 0)
    (:RELATIVE . 1))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'ThrottleCommand)))
    "Constants for message type 'ThrottleCommand"
  '((:ABSOLUTE . 0)
    (:RELATIVE . 1))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ThrottleCommand>) ostream)
  "Serializes a message object of type '<ThrottleCommand>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'request)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'request)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'request)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'request)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'position))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ThrottleCommand>) istream)
  "Deserializes a message object of type '<ThrottleCommand>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'request)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'request)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'request)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'request)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'position) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ThrottleCommand>)))
  "Returns string type for a message object of type '<ThrottleCommand>"
  "art_msgs/ThrottleCommand")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ThrottleCommand)))
  "Returns string type for a message object of type 'ThrottleCommand"
  "art_msgs/ThrottleCommand")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ThrottleCommand>)))
  "Returns md5sum for a message object of type '<ThrottleCommand>"
  "7d9e24314a55cc39669333e821a84049")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ThrottleCommand)))
  "Returns md5sum for a message object of type 'ThrottleCommand"
  "7d9e24314a55cc39669333e821a84049")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ThrottleCommand>)))
  "Returns full string definition for message of type '<ThrottleCommand>"
  (cl:format cl:nil "# ART throttle controller command message~%~%# $Id$~%~%Header  header~%~%# request types~%uint32 Absolute = 0    # set absolute position: 0.0 is off, 1.0 is fully on~%uint32 Relative = 1    # change relative to current setting, [-1.0 to 1.0]~%~%uint32  request                # request type~%float32 position               # requested position~%~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ThrottleCommand)))
  "Returns full string definition for message of type 'ThrottleCommand"
  (cl:format cl:nil "# ART throttle controller command message~%~%# $Id$~%~%Header  header~%~%# request types~%uint32 Absolute = 0    # set absolute position: 0.0 is off, 1.0 is fully on~%uint32 Relative = 1    # change relative to current setting, [-1.0 to 1.0]~%~%uint32  request                # request type~%float32 position               # requested position~%~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ThrottleCommand>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ThrottleCommand>))
  "Converts a ROS message object to a list"
  (cl:list 'ThrottleCommand
    (cl:cons ':header (header msg))
    (cl:cons ':request (request msg))
    (cl:cons ':position (position msg))
))
