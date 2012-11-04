#!/bin/bash

# Author: Jonah Miller
# File: gdp.sh is a shell script that enables the use of
# The CSCI1300 and dbg.exe debugger packages for Windows
# through the bash command line.

# The CSCI1300 home directory
CSDIR=/home/jonah/myscripts/cs1300

# Set variables
EMACS_HOME=$CSDIR/emacs/
C_INCLUDE_PATH=$CSDIR/include/
CPLUS_INCLUDE_PATH=$CSDIR/include/
LIBRARY_PATH=$CSDIR/lib/
GCC_EXEC_PREFIX=$CSDIR/lib/gcc-lib/
BISON_SIMPLE=$CSDIR/share/bison.simple
BISON_HAIRY=$CSDIR/share/bison.hairy
PATH=$PATH:$CSDIR/bin:$CSDIR/lib/gcc-lib/mingw32/3.3.1
BGI_LOCATION=$CSDIR/bin/bgi++.exe

# Program locations
WORKING_DIRECTORY=$PWD

# Exports variables
export CSDIR
export EMACS_HOME
export C_INCLUDE_PATH
export CPLUS_INCLUDE_PATH
export LIBRARY_PATH
export GCC_EXEC_PREFIX
export BISON_SIMPLE
export BISON_HAIRY
export PATH

# Change directory into bin folder where everything works
# cd $CSDIR/bin

# Runs the program
wineconsole --backend=curses $CSDIR/bin/gdb.exe --annotate=3 "Z:$WORKING_DIRECTORY/$1"

# Change directory back to where you were
cd $WORKING_DIRECTORY
