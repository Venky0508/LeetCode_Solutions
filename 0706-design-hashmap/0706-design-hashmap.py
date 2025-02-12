class MyHashMap:

    def __init__(self):
        self.myMap = {}

    def put(self, key: int, value: int) -> None:
        if key not in self.myMap:
            self.myMap[key] = value
        else:
            self.myMap[key] = value

    def get(self, key: int) -> int:
        if key not in self.myMap:
            return -1
        return self.myMap[key]
        
    def remove(self, key: int) -> None:
        if key in self.myMap:
            del self.myMap[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)