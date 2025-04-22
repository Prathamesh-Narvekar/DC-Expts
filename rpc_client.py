from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading

# Function the server can call to send a message
class ClientFunctions:
    def receive_message(self, msg):
        print(f"Server: {msg}")
        return True

def run_client_server():
    server = SimpleXMLRPCServer(("localhost", 8001), allow_none=True, logRequests=False)
    server.register_instance(ClientFunctions())
    print("Client RPC listening on port 8001...")
    server.serve_forever()

# Run client-side RPC server in background
threading.Thread(target=run_client_server, daemon=True).start()

# Connect to server RPC
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Client sends message to server
while True:
    msg = input("Client (you): ")
    server.receive_message(msg)
