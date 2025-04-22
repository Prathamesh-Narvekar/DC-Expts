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
