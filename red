#!/bin/sh
# Night vision!
# Depends on xcalib.
#
# This script is public domain.

red() {
	case $1 in
	on)
		xcalib -green .1 0 1 -alter
		xcalib -blue .1 0 1 -alter
		;;
	off)
		xcalib -clear
		;;
	*)
		echo Usage: \"red on\" or \"red off\"
		;;
	esac;
}

red $1
