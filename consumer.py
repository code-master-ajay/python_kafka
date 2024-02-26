from confluent_kafka import Producer, Consumer
import random

c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'mygroup'})
c.subscribe(['mytopic'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print('Error: {}'.format(msg.error()))
        continue

    print('Received message: {}'.format(msg.value().decode('utf-8')))