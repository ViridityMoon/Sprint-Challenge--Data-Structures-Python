class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None]*capacity
        self.current_index = 0

    def append(self, item):
        print(self.current_index)
        self.data[self.current_index] = item
        if (self.current_index+1) == self.capacity:    
            self.current_index = 0
        else:
            self.current_index += 1

    def get(self):
        new_list = []*self.capacity
        for x in self.data:
            if self.data.index(x) != None:
                new_list.append(x)
        return [a for a in new_list if a != None]