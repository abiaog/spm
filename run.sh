#!/bin/bash

PROJECT_NAME=$1
tj3client add $PROJECT_NAME.tjp
if [ $? -eq 0 ]
then
	echo "-------- Run success, ready to push! --------"
	./push.sh
fi
