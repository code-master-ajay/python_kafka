import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from confluent_kafka import Consumer
from confluent_kafka import Consumer
import json

c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'mygroup'})
c.subscribe(['mytopic'])

def consume_messages():
    while True:
        msg = c.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue
        
        data = msg.value().decode('utf-8').replace("'", '"')
        # print(f"Received message: {data}")
        # print(f"Type of data: {type(data)}") 
        data_dict = json.loads(data)

        # Extract data point from message value
        price = float(data_dict['price'])
        timestamp = int(data_dict['timestamp'])

        print(f"Price: {price}")
        print(f"Timestamp: {timestamp}")

        # Update the graph with the new data point


    #     # Extract data point from message value
    #     data_point = float(msg.value().decode('utf-8'))

    #     # Update the graph with the new data point
    #     # You may need to modify this logic based on your specific graph updating requirements
    #     x = [1, 2, 3, 4, 5]  # Example x-axis values
    #     y = [10, 20, 30, 40, 50]  # Example y-axis values
    #     x.append(len(x) + 1)  # Assuming x-axis represents time or sequence
    #     y.append(data_point)
    #     update_graph(x, y)
    # # Kafka consumer logic
    # # Consume messages from Kafka and update the graph


def main():
    # Create Tkinter window
    root = tk.Tk()
    root.title("Kafka Consumer Graph")

    # Create matplotlib figure
    fig = Figure(figsize=(6, 4))
    ax = fig.add_subplot(111)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')

    # Create Tkinter canvas for embedding matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Run Tkinter event loop
    root.mainloop()

    # Start consuming messages from Kafka
    consume_messages()



if __name__ == "__main__":
    main()
