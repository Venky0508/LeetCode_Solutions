class TimeMap:

    def __init__(self):
        self.dataMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dataMap:
            self.dataMap[key] = []
            self.dataMap[key].append((timestamp, value))
        else:
            self.dataMap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dataMap:
            return ""
        
        else:
            dataList = self.dataMap[key]
            i = len(dataList) - 1
            while i >= 0:
                data = dataList[i]
                time = data[0]
                if time <= timestamp:
                    return data[1]
                i -= 1

            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)