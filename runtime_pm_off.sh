#!/bin/sh -e
### BEGIN INIT INFO
# Provides:          shutdownfixes.sh 
# Required-Start:    
# Required-Stop:     
# X-Stop-After:      $network
# Default-Start:     
# Default-Stop:      0
# Short-Description: Fixes shutdown-to-reboot glitch.
# Description:       Fixes shutdown-to-reboot glitch.
### END INIT INFO

PATH="/sbin:/bin"

echo -n "Preparing PCI busses for shutdown..."
for i in /sys/bus/pci/devices/*/power/control; do
  echo on > $i
done
echo "done."

echo -n "Removing e1000e module..."
lsmod | grep -q e1000e && rmmod e1000e
echo "done."