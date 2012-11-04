#!/bin/sh 
#
# Author: Jonah Miller 
#
# A script to act as a workaround for the bug in the runtime power
# management module, which causes thinkpad laptops to restart after
# shutting down.

# Bus list for the runtime power management module. Probably shouldn't
# touch this.
buslist="pci spi i2c"

for bus in $buslist; do
    for i in /sys/bus/$bus/devices/*/power/control; do
        echo on > $i
    done
done