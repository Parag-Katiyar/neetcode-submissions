from bisect import bisect_right

class TimeMap:

    def __init__(self):
        # Store format: { key : [[timestamp1, value1], [timestamp2, value2]] }
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        # Timestamps are strictly increasing per LeetCode constraints
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        history = self.store[key]
        
        # bisect_right searches for the first element greater than target.
        # Since history is a list of lists, we use the key parameter 
        # to compare only the timestamp (index 0).
        idx = bisect_right(history, timestamp, key=lambda x: x[0])
        
        # If idx is 0, all recorded timestamps are greater than the target
        if idx == 0:
            return ""
            
        # The largest timestamp <= target is at index idx - 1
        return history[idx - 1][1]

