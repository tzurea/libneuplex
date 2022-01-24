#!/bin/bash

while true
do
  for i in {1..4}
  do
	  echo "Starting 25 minute session"
    sleep 25m
	  echo "Starting break"
	  notify-send "Time to take a short break"
	  sleep 5m
	  notify-send "Time to get back to work"
  done
  notify-send "Time for a long break"
  sleep 15m
  notify-send "Time to work"
done
