#!/bin/bash

# $1: subtopic ( a or b)

topic=$1
echo "This client get messages. (TOPIC: $topic)"
echo "Waiting for messages... (Cancel: Ctrl+C)"

mosquitto_sub -h localhost -t "$topic"



