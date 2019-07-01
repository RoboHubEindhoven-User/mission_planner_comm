#ifndef OBJECT_IDENTIFIER_H_
#define OBJECT_IDENTIFIER_H_

#include <string>

namespace mission_data
{
struct ObjectIdentifier
{
    int         id;
    int         instance_id;
    int         type;
    std::string description;

    ObjectIdentifier(int instance_id = 0, int type = 0, std::string description = "")
        : id(0), type(type), description(description) {}
};
} // namespace mission_data

#endif /* OBJECT_IDENTIFIER_H_ */