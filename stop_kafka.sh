#!/bin/bash


. $(pwd)/.env_file


# go to kafka directory
cd $KAFKA_PATH

# stop any running kafka broker
bin/kafka-server-stop.sh