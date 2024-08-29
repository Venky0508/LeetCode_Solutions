class RecentCounter:
    
    def __init__(self):
        self.request = []

    def ping(self, t: int) -> int:
        self.request.append(t)
        curr = [(t-3000), t]
        count = 0
        for i in self.request:
            if curr[0] <= i <= curr[1]:
                count += 1
        return count
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)