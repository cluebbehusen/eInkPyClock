#!/bin/sh

runscript() {
	python3 eInkPyClock.py
}

cd /home/pi/eInkPyClock
while true;
do
	runscript
	sleep 3m
done
