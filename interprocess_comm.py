import threading
import queue
import time

# Create a shared queue for communication
message_queue = queue.Queue()

# Worker thread function - receives messages from the queue
def worker_thread(name):
    while True:
        message = message_queue.get()  # Block until a message is available
        if message == "EXIT":
            print(f"{name} - Exiting...")
            break
        print(f"{name} received message: {message}")
        time.sleep(1)

# Producer thread function - sends messages to the queue
def producer_thread():
    for i in range(5):
        msg = f"Message {i}"
        print(f"Producer sending: {msg}")
        message_queue.put(msg)  # Put message in the queue
        time.sleep(1)

    # Send exit signal to worker threads
    message_queue.put("EXIT")
    message_queue.put("EXIT")

# Create and start worker threads
worker1 = threading.Thread(target=worker_thread, args=("Worker 1",))
worker2 = threading.Thread(target=worker_thread, args=("Worker 2",))

worker1.start()
worker2.start()

# Start the producer thread
producer = threading.Thread(target=producer_thread)
producer.start()

# Wait for all threads to finish
producer.join()
worker1.join()
worker2.join()

print("All threads have finished.")
