cmake_minimum_required(VERSION 2.8.3)
project(mission_data_types)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
    roscpp
    rospy
)

catkin_python_setup()


include_directories(include
  ${catkin_INCLUDE_DIRS}
)

# set(CMAKE_CXX_FLAGS "-ljansson ${CMAKE_CXX_FLAGS}")
# PROTOBUF_GENERATE_CPP(PROTO_SRC PROTO_HEADER proto/location_identifier.proto)
# ADD_LIBRARY(proto ${PROTO_HEADER} ${PROTO_SRC})

file(GLOB SRCS_FILES
       "src/*.cpp"
      #  "include/mission_data_types/json2pb/*.cc"
       )

## Declare a C++ library
add_library(mission_data
  ${SRCS_FILES}
)

target_link_libraries(mission_data ${catkin_LIBRARIES})

catkin_package(
    INCLUDE_DIRS include
    LIBRARIES mission_data
    CATKIN_DEPENDS roscpp rospy
)