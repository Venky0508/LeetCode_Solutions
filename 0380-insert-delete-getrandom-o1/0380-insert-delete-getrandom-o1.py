import random

class RandomizedSet:

    def __init__(self):
        self.randomSet = []

    def insert(self, val: int) -> bool:
        if val not in self.randomSet:
            self.randomSet.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.randomSet:
            return False
        else:
            for i in range(len(self.randomSet)):
                if self.randomSet[i] == val:
                    self.randomSet = self.randomSet[:i] + self.randomSet[i+1:]
                    break
            return True
        

    def getRandom(self) -> int:
        return random.choice(self.randomSet)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()