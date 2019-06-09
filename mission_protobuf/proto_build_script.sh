#!/bin/bash -       
#title           :proto_build_script.sh
#description     :This script will execute the CMakeList.txt to compile protobuf files to c++ and python files.
#author		     :Thierry Zinkeng
#date            :04-06-2019
#version         :0.1    
#usage		     :sh proto_build_script.sh or bash proto_build_script.sh
#==============================================================================

DIRECTORY_NAME="build"

while true; do

echo "\n[INFO]=> Check if build directory exist"

if [ ! -d $DIRECTORY_NAME ]; then
    echo "\n[INFO]=> Creating build directory"
    mkdir $DIRECTORY_NAME
else
    echo "\n[INFO]=> " $DIRECTORY_NAME " directory already exists" 1>&2

    echo "\n[INFO]=> Navigate to build directory\n"
    cd build

    echo "\n[INFO]=> cmake to add make configurations\n"
    cmake ..

    echo "\n[INFO]=> compiling with make\n"
    make

    echo "\n[INFO]=> Exit build directory\n"
    cd ..

    break
fi

done
