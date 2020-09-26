class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []
        self.current = 0

    def append(self, item):
        if len(self.list) < self.capacity:
            self.list.append(item)
        elif len(self.list) == self.capacity:
            self.list[self.current] = item
            self.current = (self.current + 1) % self.capacity

    def get(self):
        return self.list