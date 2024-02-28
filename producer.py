from confluent_kafka import Producer
from fake_data_generator import generate_stock_data
from multiprocessing import Pool, cpu_count

def produce_stock_data(symbol):
    p = Producer({'bootstrap.servers': 'localhost:9092'})
    for data in generate_stock_data(symbol, start_price, num_ticks):
        p.produce('mytopic', str(data))
    p.flush()

# Define parameters
symbols = ["AAPL", "GOOGL", "MSFT"]  # List of all 100 stocks
start_price = 150.0  # Starting price
num_ticks = 1000 # Number of data points per symbol

# Determine the number of CPU cores
num_cores = cpu_count()
print("Number of cores: {}".format(num_cores))

# Create a pool of worker processes
with Pool(processes=num_cores) as pool:
    # Map symbols to worker processes
    pool.map(produce_stock_data, symbols)

print("Produced {} messages for each symbol to topic mytopic".format(num_ticks * len(symbols)))
