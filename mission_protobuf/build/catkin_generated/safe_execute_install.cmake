execute_process(COMMAND "/home/zinki/workspace/catkin_ws/src/mission_planner_comm/mission_protobuf/build/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/zinki/workspace/catkin_ws/src/mission_planner_comm/mission_protobuf/build/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
