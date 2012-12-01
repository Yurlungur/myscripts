#!/bin/sh

# This is a script to partition a large folder into many smaller ones.
# Usage:
# bash partition_folder.sh /path/to/folder/you/want/to/partition
# The folder will shrink to folders each containing 1000 files.

FOLDER_NAME="FOLDER"
FOLDER_NUMBER=0

FOLDER_SIZE=1000

echo 'Partitioning folder...'

while [ $(ls $1 | wc -l) -gt $FOLDER_SIZE ]; do # iterate through the loop while the folder is too big.
    mkdir $1/$FOLDER_NAME$FOLDER_NUMBER # make a subfolder to contain files
    for i in $( ls -U $1 | head -n $FOLDER_SIZE ); do # Take the first 1000 files and move them into the subfolder
	cp $1/$i $1/$FOLDER_NAME$FOLDER_NUMBER 
	if [ $? != 0 ]; then # if the folder to be copied was a directory, don't copy it.
	    rm $1/$i
	else # Otherwise do.
	    exit $?
	fi 
    done
    FOLDER_NUMBER=$(expr $FOLDER_NUMBER + 1)
done

echo 'Done!'
