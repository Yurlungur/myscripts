#!/bin/bash

# Author: Matthew Lawson
# Time-stamp: <2014-01-01 18:14:52 (jonah)>

#This script toggles on and off an external monitor
#----------------------------------------------------------------------

# Change IN and out to the inputs given if you type "xrandr" with no
# arguments into the shell.
IN="LVDS1"
EXT="VGA1"

if (xrandr | grep "$EXT" | grep "+"); then
    xrandr --output $EXT --off --output $IN --auto
else
if (xrandr | grep "$EXT" | grep " connected"); then
    xrandr --output $IN --off --output $EXT --auto
fi
fi