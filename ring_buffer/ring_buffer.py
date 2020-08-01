class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.values = [None] * self.capacity
        self.oldest = 0

    def append(self, item):
        self.values[self.oldest] = item
        if self.oldest == self.capacity - 1:
            self.oldest = 0
        else:
            self.oldest += 1

    def get(self):
        return [value for value in self.values if value is not None]
