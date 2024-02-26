#!/bin/bash

# go to kafka directory
cd /home/tops/kafka_2.12-3.6.1

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