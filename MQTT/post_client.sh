#!/bin/bash

function post_message
{
	# $1: topic
	# $2: message
	echo -e "TOPIC: $1 \t MESSAGE: $2"
	mosquitto_pub -h localhost -t "$1" -m "$2"
}

echo "This script will post messages in the local MQTT broker."

sleep 5
post_message "test" "DATA_test"
sleep 5
post_message "test/a/a" "DATA_test-a-a"
sleep 5
post_message "test/a/b" "DATA_test-a-b"
sleep 5
post_message "test/b/a" "DATA_test-b-a"
sleep 5
post_message "test/b/b" "DATA_test-b-b"
sleep 5
post_message "test/x/y/a" "DATA_test-x-y-a"
