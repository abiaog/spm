#!/bin/bash

for i in $(pgrep tj);
do 
	echo $i
	pids=$(ps -o pid= -p $i)
	for j in $pids;
	do
		echo $j
		kill -9 $j
	done
done
