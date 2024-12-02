class MedianFinder:

    def __init__(self):
        self.dataStream = []

    def addNum(self, num: int) -> None:
        for i in range(len(self.dataStream)):
            if(num<=self.dataStream[i]):
                self.dataStream.insert(i,num)
                return 
        self.dataStream.append(num)
        

    def findMedian(self) -> float:
        total = len(self.dataStream)
        if total % 2 == 0:
            ind1 = total//2
            ind2 = ind1 - 1
            return (self.dataStream[ind1] + self.dataStream[ind2])/2
        
        else:
            index = total//2
            return self.dataStream[index]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()