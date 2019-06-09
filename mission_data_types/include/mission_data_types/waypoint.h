#ifndef WAYPOINT_H_
#define WAYPOINT_H_

#include <string>
#include "geometry.h"
#include "service_area.h"

struct Location
{
    int type;
    int instance_id;
    std::string description;

    Location(int type = 0, int instance_id = 0, std::string description = "")
    : type(type), instance_id(instance_id), description(description){}

};

struct Waypoint
{
    Location        location;
    geometry::Pose  pose;
    ServiceArea     service_area;

    Waypoint(Location location = {0,0,""}, geometry::Pose pose = {{0,0,0}, {0,0,0,0}}, ServiceArea service_area = {0,0,0,0,0,0})
    :location(location), pose(pose), service_area(service_area){}

};


#endif /* WAYPOINT_H_ */