cmake_minimum_required(VERSION 2.8.3)
#include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)
project(art_msgs)
find_package(catkin REQUIRED COMPONENTS
  message_generation
  nav_msgs
  geometry_msgs
  std_msgs
  sensor_msgs
)

#rosbuild_init()  # to be removed in catkin_make

#set the default path for built executables to the "bin" directory
#set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
#set the default path for built libraries to the "lib" directory
#set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

#uncomment if you have defined messages
#rosbuild_genmsg()
add_message_files(
    FILES
    NavigatorState.msg
    ArtHertz.msg
    SteeringState.msg BrakeState.msg CarControl.msg Shifter.msg Epsilon.msg ThrottleState.msg Behavior.msg CarDrive.msg LaneMarking.msg IOadrState.msg ThrottleCommand.msg BrakeCommand.msg PilotState.msg ArtQuadrilateral.msg SteeringCommand.msg NavigatorCommand.msg Gear.msg GpsInfo.msg CarDriveStamped.msg Observation.msg ArtLanes.msg LearningCommand.msg ObservationArray.msg ArtVehicle.msg PilotBehavior.msg RoadState.msg MapID.msg SteeringDiagnostics.msg EstopState.msg Order.msg IOadrCommand.msg DriverState.msg Conversions.msg WayPoint.msg CarCommand.msg NavigatorState.msg ArtHertz.msg SteeringState.msg BrakeState.msg CarControl.msg Shifter.msg Epsilon.msg ThrottleState.msg Behavior.msg CarDrive.msg LaneMarking.msg IOadrState.msg ThrottleCommand.msg BrakeCommand.msg PilotState.msg ArtQuadrilateral.msg SteeringCommand.msg NavigatorCommand.msg Gear.msg GpsInfo.msg CarDriveStamped.msg Observation.msg ArtLanes.msg LearningCommand.msg ObservationArray.msg ArtVehicle.msg PilotBehavior.msg RoadState.msg MapID.msg SteeringDiagnostics.msg EstopState.msg Order.msg IOadrCommand.msg DriverState.msg Conversions.msg WayPoint.msg CarCommand.msg
)


generate_messages(
    DEPENDENCIES
    nav_msgs geometry_msgs std_msgs sensor_msgs)
    
    
include_directories(
  ${catkin_INCLUDE_DIRS}
)
#uncomment if you have defined services
#rosbuild_gensrv()
