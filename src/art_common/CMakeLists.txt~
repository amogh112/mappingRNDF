
cmake_minimum_required(VERSION 2.8.3)
project(art_common)

find_package(catkin REQUIRED COMPONENTS angles roscpp tf dynamic_reconfigure)
find_package(Boost REQUIRED COMPONENTS thread)
include_directories(include ${Boost_INCLUDE_DIR} ${catkin_INCLUDE_DIRS})

#set the default path for built executables to the "bin" directory
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
#set the default path for built libraries to the "lib" directory
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

generate_dynamic_reconfigure_options(
	cfg/CameraTransform.cfg

)
catkin_package(
    DEPENDS
    CATKIN_DEPENDS art_msgs
    INCLUDE_DIRS include
    LIBRARIES art_common_LIBRARIES
)             
include_directories( ${catkin_INCLUDE_DIRS}
  ${dynamic_reconfigure_PACKAGE_PATH}/cmake/cfgbuild.cmake
)

install(DIRECTORY include/art/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
  FILES_MATCHING PATTERN "*.h"
  PATTERN ".svn" EXCLUDE)


add_executable(vehicle_configurable_tf src/vehicle_configurable_tf.cc)
target_link_libraries(vehicle_configurable_tf ${catkin_LIBRARIES})
#add_dependencies(block_manipulation turtlebot_arm_block_manipulation_gencpp)
add_dependencies(vehicle_configurable_tf ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS} ${catkin_LIBRARIES} ${PROJECT_NAME}_gencfg)

add_executable(vehicle_static_tf src/vehicle_static_tf.cc)
target_link_libraries(vehicle_static_tf ${catkin_LIBRARIES})
add_dependencies(vehicle_static_tf ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS} ${catkin_LIBRARIES} ${PROJECT_NAME}_gencfg)


