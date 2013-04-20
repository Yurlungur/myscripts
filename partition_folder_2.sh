#!/bin/sh

# This is a script to partition a large folder into many smaller ones.
# Usage:
# bash partition_folder.sh foldersize /path/to/folder/you/want/to/partition
# The folder will shrink to folders each containing foldersize files.

FOLDER_NAME="FOLDER"
FOLDER_NUMBER=0

FOLDER_SIZE=$1
FOLDER_TO_PARTITION=$2

echo 'Partitioning folder...'

while [ $(ls $FOLDER_TO_PARTITION | wc -l) -gt $FOLDER_SIZE ]; do # iterate through the loop while the folder is too big.
    mkdir $FOLDER_TO_PARTITION/$FOLDER_NAME$FOLDER_NUMBER # make a subfolder to contain files
    for i in $( ls -U $FOLDER_TO_PARTITION | head -n $FOLDER_SIZE ); do # Take the first 1000 files and move them into the subfolder
	cp $FOLDER_TO_PARTITION/$i $FOLDER_TO_PARTITION/$FOLDER_NAME$FOLDER_NUMBER 
	if [ $? != 0 ]; then # if the folder to be copied was a directory, don't copy it.
	    rm $FOLDER_TO_PARTITION/$i
	else # Otherwise do.
	    exit $?
	fi 
    done
    FOLDER_NUMBER=$(expr $FOLDER_NUMBER + 1)
done

echo 'Done!'
