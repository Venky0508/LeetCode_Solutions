import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.memory = collections.OrderedDict()
        self.maxCapacity = capacity
      

    def get(self, key: int) -> int:
        # for k, v in self.memory.items():
        #     print(f"{k} : {v}")
        if key in self.memory:
            self.memory.move_to_end(key)
            return self.memory[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.memory:
            if len(list(self.memory.keys())) < self.maxCapacity:
                self.memory[key] = value
            else:
                self.memory.popitem(last = False)
                self.memory[key] = value
        else:
            self.memory.move_to_end(key)
            self.memory[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)