#ifndef SERVICE_AREA_H_
#define SERVICE_AREA_H_

struct ServiceArea
{
    int id;
    double length;
    double width;
    double height;
    double diameter;
    double tilt_angle;

    ServiceArea(double id = 0, double length = 0, double width = 0, double height = 0, double diameter = 0, double tilt_angle = 0)
    : id(id), length(length), width(width), height(height), diameter(diameter), tilt_angle(tilt_angle){}
};

#endif /* SERVICE_AREA_H_ */