#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/zinki/workspace/catkin_ws/src/mission_planner_comm/mission_protobuf"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/usr/local/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/usr/local/lib/python2.7/dist-packages:/home/zinki/workspace/catkin_ws/src/mission_planner_comm/mission_protobuf/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/zinki/workspace/catkin_ws/src/mission_planner_comm/mission_protobuf/build" \
    "/usr/bin/python" \
    "/home/zinki/workspace/catkin_ws/src/mission_planner_comm/mission_protobuf/setup.py" \
    build --build-base "/home/zinki/workspace/catkin_ws/src/mission_planner_comm/mission_protobuf/build" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/usr/local" --install-scripts="/usr/local/bin"
