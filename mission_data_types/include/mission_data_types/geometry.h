#ifndef GEOMETRY_H_
#define GEOMETRY_H_

namespace geometry
{
struct Pose
{
    struct Point
    {
        double x;
        double y;
        double z;
        Point(double x = 0, double y = 0, double z = 0) 
        : x(x), y(y), z(z){}
    } point;

    struct Quaternion
    {
        double x;
        double y;
        double z;
        double w;
        Quaternion(double x = 0, double y = 0, double z = 0, double w = 0) 
        : x(x), y(y), z(z), w(w){}
    };

    Point position;
    Quaternion orientation;
    Pose(Point position = {0,0,0}, Quaternion orientation = {0,0,0,0}) 
    : position(position), orientation(orientation) {}
};
} // namespace geometry

#endif /* GEOMETRY_H_ */
