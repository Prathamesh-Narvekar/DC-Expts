from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading

# Function the client can call to send a message
class ServerFunctions:
    def receive_message(self, msg):
        print(f"Client: {msg}")
        return True

def run_server():
    server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True, logRequests=False)
    server.register_instance(ServerFunctions())
    print("Server RPC listening on port 8000...")
    server.serve_forever()

# Run server in a background thread
threading.Thread(target=run_server, daemon=True).start()

# Connect to client RPC
client = xmlrpc.client.ServerProxy("http://localhost:8001/")

# Server sends message to client
while True:
    msg = input("Server (you): ")
    client.receive_message(msg)
