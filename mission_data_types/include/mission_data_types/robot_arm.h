#ifndef ROBOT_ARM_H_
#define ROBOT_ARM_H_

#include <string>

namespace robot_arm {

struct JointPose
{
    int id;
    std::string description;
    double joint_1;
    double joint_2;
    double joint_3;
    double joint_4;
    double joint_5;
    double joint_6;

    JointPose(double id = 0, std::string description = "", double joint_1 = 0, double joint_2 = 0, double joint_3 = 0, double joint_4 = 0, double joint_5 = 0, double joint_6 = 0)
    : id(id), description(description), joint_1(joint_1), joint_2(joint_2), joint_3(joint_3), joint_4(joint_4), joint_5(joint_5), joint_6(joint_6) {}
};

} /* namespace robot_arm */

#endif /* ROBOT_ARM_H_ */