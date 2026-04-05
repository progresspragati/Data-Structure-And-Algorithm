import heapq


class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()
        n = len(self.data)
        if n & 1:
            return self.data[n//2]
        else:
            return (self.data[n//2] + self.data[n//2-1])/2
    
class MedianFinderUsingHeapq:
    def __init__(self):
        self.small = []
        self.large = []
    
    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large[0])
            heapq.heappush(self.small, -1 * val)
    
    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.large) < len(self.small):
            return -1 * self.small[0]
        return (self.large[0] + -1 * self.small[0])/2
        
result = MedianFinder()
result.addNum(1)
result.addNum(7)
result.addNum(5)
result.addNum(6)
print(result.findMedian())
result1 = MedianFinderUsingHeapq()
result1.addNum(1)
result1.addNum(7)
result1.addNum(5)
result1.addNum(6)
print(result1.findMedian())