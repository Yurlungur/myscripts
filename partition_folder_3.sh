#!/bin/sh

# This is a script to partition a large folder into many smaller ones.
# Usage:
# bash partition_folder.sh foldersize /path/to/folder/you/want/to/partition
# The folder will shrink to folders each containing foldersize files.

FOLDER_NAME="FOLDER"
FOLDER_NUMBER=0

FOLDER_SIZE=$1
FOLDER_TO_PARTITION=$(realpath $2)

# This ensures that new folders are numbered higher than older ones.
while [ -d $FOLDER_TO_PARTITION/$FOLDERNAME$FOLDER_NUMBER ]; do
    FOLDER_NUMBER=$(expr $FOLDER_NUMBER + 1)
done

echo "Partitioning folder into subfolders of $FOLDER_SIZE."
echo "The folder to partition is:"
echo $FOLDER_TO_PARTITION
echo "partitioning..."


while [ $(ls -l $FOLDER_TO_PARTITION | grep -v ^d | wc -l) -gt $FOLDER_SIZE ]; do # iterate through the loop while the folder is too big.
    mkdir $FOLDER_TO_PARTITION/$FOLDER_NAME$FOLDER_NUMBER # make a subfolder to contain files
    for i in $( ls -t $FOLDER_TO_PARTITION | tail -n $FOLDER_SIZE ); do # Take the first 1000 files and move them into the subfolder
	if [ -f $FOLDER_TO_PARTITION/$i ]; then # If the file is regular, move it over.
	    mv $FOLDER_TO_PARTITION/$i $FOLDER_TO_PARTITION/$FOLDER_NAME$FOLDER_NUMBER
	fi
    done
    FOLDER_NUMBER=$(expr $FOLDER_NUMBER + 1)
done

echo 'Done!'
