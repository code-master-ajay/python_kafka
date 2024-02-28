#!/bin/bash

# load environment variables
. $(pwd)/.env_file


# go to kafka directory
cd $KAFKA_PATH

# stop any running kafka broker
bin/kafka-server-stop.sh


# Start Zookeeper
echo "Starting Zookeeper..."
bin/zookeeper-server-start.sh config/zookeeper.properties &

# Start Kafka Broker
echo "Starting Kafka Broker..."
bin/kafka-server-start.sh config/server.properties

sleep 5
echo "Kafka setup completed."