cmake_minimum_required(VERSION 2.8.3)
project(mission_protobuf)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  # geometry_msgs
)
find_package(Protobuf REQUIRED)

catkin_python_setup()



include_directories(include
  ${catkin_INCLUDE_DIRS}
  ${PROTOBUF_INCLUDE_DIRS}
)

# set(CMAKE_CXX_FLAGS "-ljansson ${CMAKE_CXX_FLAGS}")
# PROTOBUF_GENERATE_CPP(PROTO_SRC PROTO_HEADER proto/location_identifier.proto)
# ADD_LIBRARY(proto ${PROTO_HEADER} ${PROTO_SRC})

file(GLOB ALL_PROTO_SRCS
       "include/mission_protobuf/*.cc"
      #  "include/mission_protobuf/json2pb/*.cc"
       )

## Declare a C++ library
add_library(mission_planner_proto
  ${ALL_PROTO_SRCS}
)
target_link_libraries(mission_planner_proto ${PROTOBUF_LIBRARIES} ${catkin_LIBRARIES})

catkin_package(
    INCLUDE_DIRS include
    LIBRARIES mission_planner_proto
    CATKIN_DEPENDS
        roscpp
)


## Add cmake target dependencies of the library
## as an example, code may need to be generated before libraries
## either from message generation or dynamic reconfigure
# add_dependencies(mission_protobuf ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Declare a C++ executable
# add_executable(mission_protobuf_node src/mission_example_node.cpp)

## Add cmake target dependencies of the executable
## same as for the library above
# add_dependencies(mission_protobuf_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

# add_dependencies(mission_protobuf_node mission_protobuf_node_generate_messages_cpp)

## Specify libraries to link a library or executable target against
# target_link_libraries(mission_protobuf_node
#   ${catkin_LIBRARIES}
#   mission_planner_proto
#   ${PROTOBUF_LIBRARIES}
# )

# #############
# ## Install ##
# #############

# # all install targets should use catkin DESTINATION variables
# # See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

# ## Mark executable scripts (Python etc.) for installation
# ## in contrast to setup.py, you can choose the destination
# # install(PROGRAMS
# #   scripts/my_python_script
# #   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# # )

# ## Mark executables and/or libraries for installation
# # install(TARGETS mission_protobuf mission_protobuf
# #   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
# #   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
# #   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# # )

# ## Mark cpp header files for installation
# install(DIRECTORY include/${PROJECT_NAME}/
#   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
#   FILES_MATCHING PATTERN "*.pb.h"
#   PATTERN ".svn" EXCLUDE)

# ## Mark other files for installation (e.g. launch and bag files, etc.)
# # install(FILES
# #   # myfile1
# #   # myfile2
# #   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# # )
#**************************************************************************************

file(GLOB ALL_PROTO_SRCS "${PROJECT_SOURCE_DIR}/proto/*.proto")

file(TO_NATIVE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/proto PROTOMODEL_PATH)
file(TO_NATIVE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/include/mission_protobuf PROTOBINDING_PATH)
set(PROTOBUF_OUTPUT_DIR_PY "${PROJECT_SOURCE_DIR}/src/mission_protobuf")


file(GLOB DATAMODEL_PROTOS ${ALL_PROTO_SRCS})
message( "\nSource Folder:             " ${PROTOMODEL_PATH})
message( "Destination Folder C++:    " ${PROTOBINDING_PATH})
message( "Destination Folder Python: " ${PROTOBUF_OUTPUT_DIR_PY})
message( "\n" )

foreach(proto ${DATAMODEL_PROTOS})

  file(TO_NATIVE_PATH ${proto} proto_native)

  # c++ generation
  execute_process(COMMAND ${PROTOBUF_PROTOC_EXECUTABLE} --proto_path=${PROTOMODEL_PATH} --cpp_out=${PROTOBINDING_PATH} ${proto_native}
  RESULT_VARIABLE rv_cpp)

  # python generation
  execute_process(COMMAND ${PROTOBUF_PROTOC_EXECUTABLE} --proto_path=${PROTOMODEL_PATH} --python_out=${PROTOBUF_OUTPUT_DIR_PY} ${proto_native}
  RESULT_VARIABLE rv_py)
  
  # Optional, but that can show the user if something have gone wrong with the proto generation 
  if(${rv_cpp})
        message("Generation of data model returned ${rv} for proto ${proto_native}")
  endif()
  
  if(${rv_py})
   message("Generation of data model returned ${rv_py} for proto ${proto_native}")
  endif()

endforeach(proto)

file(GLOB PROTO_MODEL_FILES
      "${PROJECT_SOURCE_DIR}/include/mission_protobuf/*.pb.h"
      "${PROJECT_SOURCE_DIR}/include/mission_protobuf/*.pb.cc"
)

ADD_LIBRARY(mission_protobuf ${PROTO_MODEL_FILES})
# ${PROTOBUF_LIBRARIES} should be defined by FIND_PACKAGE(Protobuf REQUIRED)
TARGET_LINK_LIBRARIES(mission_protobuf ${PROTOBUF_LIBRARIES})

## Mark cpp header files for installation
install(DIRECTORY include/${PROJECT_NAME}/
   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
   FILES_MATCHING PATTERN "*.pb.h"
   PATTERN ".svn" EXCLUDE)
