from confluent_kafka import Producer, Consumer
import random
from fake_data_generator import generate_stock_data

p = Producer({'bootstrap.servers': 'localhost:9092'})


symbol = "AAPL"
start_price = 150.0
num_ticks = 3600

for data in generate_stock_data(symbol, start_price, num_ticks):
    p.produce('mytopic', str(data))


p.flush()