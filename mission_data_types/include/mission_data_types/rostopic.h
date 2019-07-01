#ifndef ROSTOPIC_H_ 
#define ROSTOPIC_H_

#include <string>

namespace rostopic {

struct Topic {
    static const std::string WaypointMarker;
    static const std::string RobotArmPose;
    static const std::string MissionTask;
    static const std::string MoveBaseFeedback;
    static const std::string JointState;
    static const std::string TodoTasks;
    static const std::string CompletedTasks;
    static const std::string CurrentTasks;
    static const std::string HolderList;
    static const std::string MissionState;
};

const std::string Topic::WaypointMarker     = "/mission_planner_comm/waypoint_marker";
const std::string Topic::RobotArmPose       = "/joint_states";
const std::string Topic::MissionTask        = "/mission_planner_comm/mission_task";
const std::string Topic::MoveBaseFeedback   = "/move_base/feedback";
const std::string Topic::JointState         = "/joint_states";
const std::string Topic::TodoTasks          = "/mission_planner_comm/todo_tasks";
const std::string Topic::CompletedTasks     = "/mission_planner_comm/completed_tasks";
const std::string Topic::CurrentTasks       = "/mission_planner_comm/current_tasks";
const std::string Topic::HolderList         = "/mission_planner_comm/holder_list";
const std::string Topic::MissionState       = "/mission_planner_comm/mission_state";

} /* namespace rostopic  */


#endif /* ROSTOPIC_H_ */