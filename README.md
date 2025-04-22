# DC-Expts

<h2>Implement a Client/server using RPC</h2>
<h3>Client file</h3>
<p>from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading

//Function the server can call to send a message
class ClientFunctions:
    def receive_message(self, msg):
        print(f"Server: {msg}")
        return True

def run_client_server():
    server = SimpleXMLRPCServer(("localhost", 8001), allow_none=True, logRequests=False)
    server.register_instance(ClientFunctions())
    print("Client RPC listening on port 8001...")
    server.serve_forever()

//Run client-side RPC server in background
threading.Thread(target=run_client_server, daemon=True).start()

//Connect to server RPC
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

//Client sends message to server
while True:
    msg = input("Client (you): ")
    server.receive_message(msg)
</p>
<h3>Server File</h3>
<P>from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading

//Function the client can call to send a message
class ServerFunctions:
    def receive_message(self, msg):
        print(f"Client: {msg}")
        return True

def run_server():
    server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True, logRequests=False)
    server.register_instance(ServerFunctions())
    print("Server RPC listening on port 8000...")
    server.serve_forever()

//Run server in a background thread
threading.Thread(target=run_server, daemon=True).start()

//Connect to client RPC
client = xmlrpc.client.ServerProxy("http://localhost:8001/")

//Server sends message to client
while True:
    msg = input("Server (you): ")
    client.receive_message(msg)
</P>
<hr>
<h2>Simulate interprocess communication using multi-thread application</h2>
<P>
import threading
import queue
import time

//Create a shared queue for communication
message_queue = queue.Queue()

//Worker thread function - receives messages from the queue
def worker_thread(name):
    while True:
        message = message_queue.get()  # Block until a message is available
        if message == "EXIT":
            print(f"{name} - Exiting...")
            break
        print(f"{name} received message: {message}")
        time.sleep(1)

//Producer thread function - sends messages to the queue
def producer_thread():
    for i in range(5):
        msg = f"Message {i}"
        print(f"Producer sending: {msg}")
        message_queue.put(msg)  # Put message in the queue
        time.sleep(1)

    # Send exit signal to worker threads
    message_queue.put("EXIT")
    message_queue.put("EXIT")

//Create and start worker threads
worker1 = threading.Thread(target=worker_thread, args=("Worker 1",))
worker2 = threading.Thread(target=worker_thread, args=("Worker 2",))

worker1.start()
worker2.start()

//Start the producer thread
producer = threading.Thread(target=producer_thread)
producer.start()

//Wait for all threads to finish
producer.join()
worker1.join()
worker2.join()

print("All threads have finished.")
</P>
<hr>
<h2>Implement at a program for Group Communication</h2>
<h3>Server File</h3>
<p>
import socket
localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024
//Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#UDPServerSocket2 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
//Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
#UDPServerSocket2.bind((localIP, localPort))
print("UDP server up and listening")
//Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    m=message.decode()
    clientMsg = "Message from Client "+m[len(m)-1]+": "+m[0:len(m)-1]
    clientIP = "Client IP Address: {}".format(address)
    print(clientMsg)
#print(clientIP)
    msgFromServer = input("Enter your message for client "+m[len(m)-1]+": ")
    bytesToSend = str.encode(msgFromServer)
//Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)
</p>
<h3>Client1 file</h3>
<P>
import socket
import time
while True:
    msgFromClient = input("Enter your message :")
    bytesToSend = str.encode(msgFromClient +"1")
    serverAddressPort = ("127.0.0.1", 20001)
    bufferSize = 1024
//Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
//Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message from Server :{}".format(msgFromServer[0].decode())
#time.sleep(5)
    print(msg)
</P>
<h3>Client2 file</h3>
<P>
import socket
import time
while True:
    msgFromClient = input("Enter your message :")
    bytesToSend = str.encode(msgFromClient +"2")
    serverAddressPort = ("127.0.0.1", 20001)
    bufferSize = 1024
//Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
//Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message from Server :{}".format(msgFromServer[0].decode())
#time.sleep(5)
    print(msg)
</P>
<h3>Client3 file</h3>
<p>
import socket
import time
while True:
    msgFromClient = input("Enter your message :")
    bytesToSend = str.encode(msgFromClient +"3")
    serverAddressPort = ("127.0.0.1", 20001)
    bufferSize = 1024
//Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
//Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message from Server :{}".format(msgFromServer[0].decode())
//time.sleep(5)
    print(msg)
</p>
<hr>
<h2>Implementation a Load Balancing Algorithm</h2>
<P>
class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0  # To keep track of the next server to use

    def get_next_server(self):
        if not self.servers:
            raise Exception("No servers available")

        # Get the server at current index
        server = self.servers[self.index]

        # Move to the next index in round-robin fashion
        self.index = (self.index + 1) % len(self.servers)

        return server

    def add_server(self, server):
        self.servers.append(server)
        print(f"Server '{server}' added.")

    def remove_server(self, server):
        if server in self.servers:
            self.servers.remove(server)
            print(f"Server '{server}' removed.")
        else:
            print(f"Server '{server}' not found.")


//Example usage
if __name__ == "__main__":
    servers = ["Server1", "Server2", "Server3"]
    lb = LoadBalancer(servers)

    for i in range(10):
        selected_server = lb.get_next_server()
        print(f"Request {i+1} is handled by {selected_server}")
</P>
<hr>
<h2>Simulate the functioning of Lamport‟s Logical Clock</h2>
<p>
class Process:
    def __init__(self, pid):
        self.pid = pid
        self.clock = 0

    def internal_event(self):
        self.clock += 1
        print(f"Process {self.pid} executes internal event. Clock = {self.clock}")

    def send_message(self, receiver):
        self.clock += 1
        print(f"Process {self.pid} sends message to Process {receiver.pid}. Clock = {self.clock}")
        receiver.receive_message(self.clock)

    def receive_message(self, timestamp):
        self.clock = max(self.clock, timestamp) + 1
        print(f"Process {self.pid} receives message. Clock updated to {self.clock}")


# Simulation
if __name__ == "__main__":
    # Create processes
    p1 = Process(1)
    p2 = Process(2)

    # Sequence of events
    p1.internal_event()          # Event in P1
    p1.send_message(p2)          # P1 sends to P2
    p2.internal_event()          # Event in P2
    p2.send_message(p1)          # P2 sends to P1
    p1.internal_event()          # Event in P1
</p>
<hr>
<h2>Implement an Election Algorithm.</h2>
<P>
class Process:
    def __init__(self, pid, is_alive=True):
        self.pid = pid
        self.is_alive = is_alive

    def start_election(self, processes):
        print(f"\nProcess {self.pid} starts an election.")
        higher_processes = [p for p in processes if p.pid > self.pid and p.is_alive]

        if not higher_processes:
            print(f"Process {self.pid} becomes the new coordinator.")
            return self.pid
        else:
            for p in higher_processes:
                print(f"Process {self.pid} sends election message to Process {p.pid}")

            # Assume the highest process will eventually win
            winner = max(higher_processes, key=lambda p: p.pid)
            return winner.start_election(processes)


# Simulation
if __name__ == "__main__":
    //Create processes with IDs
    processes = [
        Process(1),
        Process(2),
        Process(3),
        Process(4),
        Process(5),
    ]

    # Let's say process 5 (coordinator) fails
    processes[4].is_alive = False
    print("Process 5 (the current coordinator) has failed.")

    # Process 2 detects the failure and starts an election
    new_coordinator = processes[1].start_election(processes)
    print(f"\n✅ Process {new_coordinator} is elected as the new coordinator.")
</P>
