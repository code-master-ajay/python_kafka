import random
import time
from datetime import datetime, timedelta

def generate_stock_data(symbol, start_price, num_ticks, interval_seconds=1):
    current_price = start_price
    timestamp = datetime.now()

    for _ in range(num_ticks):
        # Generate a random price change
        price_change = random.uniform(-1.0, 1.0)
        current_price += price_change

        # Update timestamp
        timestamp += timedelta(seconds=interval_seconds)
        time.sleep(1)
        yield {
            'price': current_price,
            'timestamp': timestamp,
            'symbol': symbol
        }

# # Example usage
# symbol = "AAPL"
# start_price = 150.0
# num_ticks = 10

# for data in generate_stock_data(symbol, start_price, num_ticks):
#     print(data)
