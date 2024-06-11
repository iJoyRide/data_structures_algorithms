import collections

class RecentCounter:
    def __init__(self):
        # Initialize a deque to store recent ping timestamps
        self.queue = collections.deque()

    def ping(self, t):
        # Add the current ping timestamp to the queue
        self.queue.append(t)

        # Remove ping timestamps older than 3000 milliseconds
        while self.queue[0] < (t - 3000):
            self.queue.popleft()

        # Return the number of recent pings within the 3000-millisecond window
        return len(self.queue)
    
# Time: O(N)
# Space: O(1)

if __name__ == "__main__":
    recent_counter = RecentCounter()  # Create an instance of RecentCounter

    # List of ping timestamps
    t = [1, 100, 3001, 3002]

    # Iterate over the list of timestamps and print the count of recent pings
    for timestamp in t:
        print(recent_counter.ping(timestamp))

