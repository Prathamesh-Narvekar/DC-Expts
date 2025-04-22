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
    # Create processes with IDs
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
