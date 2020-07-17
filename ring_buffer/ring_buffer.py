
"""   When the ring buffer is full and a new element is inserted,
      the oldest element in the ring buffer is overwritten with the newest element.
      -
      -
      keep track of how many items are in the aray, if its full self.index is 0
      --
      --
      return all items in self.storage
          
          
"""

class RingBuffer:
    def __init__(self, capacity):
        self.capacity: int = capacity
        self.storage = []
        self.index = 0

    def append(self, item):
        if self.index >= len(self.storage):
            self.storage.append(item)
        else:
            self.storage[self.index] = item
        self.index += 1
        if self.index == self.capacity:
            self.index = 0
            
    def get(self):
        return self.storage