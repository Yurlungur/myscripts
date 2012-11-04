# This script is for cygwin to set proper variables
# On startup for CSCI1300 to work properly with cygwin
#
#
# The home directory for CSSCI1300
CSDIR='/cygdrive/c/Program Files (x86)/Colorado/cs1300'
#
# Sets the required variables.
EMACS_HOME=$CSDIR/emacs/ 
C_INCLUDE_PATH=$CSDIR/include/ 
LIBRARY_PATH=$CSDIR/lib/ 
GCC_EXEC_PREFIX=$CSDIR/lib/gcc-lib/
BISON_SIMPLE=$CSDIR/share/bison.simple
BISON_HAIRY=$CSDIR/share/bison.hairy
shell=

# Exports the required variables
export EMACS_HOME
export C_INCLUDE_PATH
export LIBRARY_PATH
export GCC_EXEC_PREFIX
export BISON_SIMPLE
export BISON_HAIRY
export shell 
