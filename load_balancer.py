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


# Example usage
if __name__ == "__main__":
    servers = ["Server1", "Server2", "Server3"]
    lb = LoadBalancer(servers)

    for i in range(10):
        selected_server = lb.get_next_server()
        print(f"Request {i+1} is handled by {selected_server}")
