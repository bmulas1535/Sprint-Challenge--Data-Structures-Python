class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.size = 0
        self.idx = 0

    def append(self, item):
        # Check if Capacity is reached
        if self.size == self.capacity:

            self.buffer[self.idx] = item
            if self.idx == self.size - 1:
                self.idx = 0
            else:
                self.idx = self.idx + 1
        else:
            self.buffer.append(item)
            self.size = self.size + 1
        return None
            
    def get(self):
        return self.buffer