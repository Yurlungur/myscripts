#!/usr/bin/env sh

MYDIR=$(pwd)

PATHS=$(realpath $@)

cd /home/jonah
for i in $PATHS; do
    echo "(push \"$i\" *filenamelist*)"
done

cd $MYDIR

