class SmallestInfiniteSet:

    def __init__(self):
        self.infiniteSet = []
        for i in range(1, 1001):
            self.infiniteSet.append(i)
        self.smallestNum = (1, 0)
        

    def popSmallest(self) -> int:
        val, idx = self.smallestNum
        self.infiniteSet = self.infiniteSet[:idx] + self.infiniteSet[idx+1:]
        if self.infiniteSet != []:
            nextMin = min(self.infiniteSet)
            pos = self.infiniteSet.index(nextMin)
            self.smallestNum = (nextMin, pos)
        else:
            self.smallestNum = (-1, -1)
        
        return val

    def addBack(self, num: int) -> None:
        if num not in self.infiniteSet:
            self.infiniteSet.append(num)
            if num <= self.smallestNum[0]:
                self.smallestNum = (num, self.infiniteSet.index(num))
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)