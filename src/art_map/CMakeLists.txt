cmake_minimum_required(VERSION 2.8.3)
project(art_map)
# Load catkin and all dependencies required for this package
# TODO: remove all from COMPONENTS that are not catkin packages.
find_package(catkin REQUIRED COMPONENTS angles geometry_msgs nav_msgs roscpp sensor_msgs tf visualization_msgs)
#find_package(art_common REQUIRED)
#include_directories(${art_common_INCLUDE_DIRS} )
find_package(Boost REQUIRED COMPONENTS thread)
include_directories(include ${Boost_INCLUDE_DIR} ${catkin_INCLUDE_DIRS})

#set the default path for built executables to the "bin" directory
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
#set the default path for built libraries to the "lib" directory
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

#add_subdirectory(src/lib)
#add_subdirectory(src/node)
## Generate added messages and services with any dependencies listed here
#generate_messages(
    #TODO DEPENDENCIES geometry_msgs std_msgs)

# TODO: fill in what other packages will need to use this package
catkin_package(
    DEPENDS 
    CATKIN_DEPENDS angles art_common art_msgs geometry_msgs nav_msgs roscpp sensor_msgs tf visualization_msgs # TODO
    INCLUDE_DIRS include # TODO include
    LIBRARIES # TODO
)

add_library(art_map
  src/FilteredPolygon.cc
  src/DrawLanes.cc
  src/gaussian.cc
  src/Graph.cc
  src/KF.cc
  src/MapLanes.cc
  src/Matrix.cc
  src/rotate_translate_transform.cc
  src/PolyOps.cc
  src/RNDF.cc
  src/SmoothCurve.cc
  src/VisualLanes.cc
  src/ZoneOps.cc
)

add_library(artmap src/DrawLanes.cc)
add_dependencies(artmap ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

include_directories( ${catkin_INCLUDE_DIRS}
  ${dynamic_reconfigure_PACKAGE_PATH}/cmake/cfgbuild.cmake
)

add_executable(maplanes src/mapl.cc)
target_link_libraries(maplanes artmap ${catkin_LIBRARIES})
add_dependencies(maplanes ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS} ${catkin_LIBRARIES})
#add_dependencies(maplanes ${${PROJECT_NAME}_EXPORTED_TARGETS}) 
#rosbuild_add_executable(rndf_lanes rndf_lanes.cc)
#target_link_libraries(rndf_lanes artmap)

add_executable(test_lanes src/test_lanes.cc )
target_link_libraries(test_lanes artmap)
add_dependencies(test_lanes ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS} ${catkin_LIBRARIES})

add_executable(getpoints src/getpoints.cc)
target_link_libraries(getpoints artmap)
add_dependencies(getpoints ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS} ${catkin_LIBRARIES})

