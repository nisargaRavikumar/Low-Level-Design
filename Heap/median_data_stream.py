import heapq

class MedianFinder:
    def __init__(self) -> None:
        self.lower_bound = []
        self.upper_bound = []

    def add_number(self,num):
        heapq.heappush(self.lower_bound, -num)
        
        if len(self.lower_bound) > len(self.upper_bound) + 1:
            val = -heapq.heappop(self.lower_bound)
            heapq.heappush(self.upper_bound, val)
        elif self.upper_bound and -self.lower_bound[0]>self.upper_bound[0]:
            val = -heapq.heappop(self.lower_bound)
            heapq.heappush(self.upper_bound, val)
        elif len(self.upper_bound) > len(self.lower_bound) + 1:
            val = heapq.heappop(self.upper_bound)
            heapq.heappush(self.lower_bound, -val)
    def findMedian(self):
        if len(self.lower_bound) > len(self.upper_bound):
            print(-self.lower_bound[0])
            return -self.lower_bound[0]
        elif len(self.lower_bound) < len(self.upper_bound):
            print(self.upper_bound[0])
            return self.upper_bound[0]
        else:
            print((-self.lower_bound[0] + self.upper_bound))
            return (-self.lower_bound[0] + self.upper_bound) // 2

obj = MedianFinder()
obj.add_number(1)
obj.add_number(3)
obj.add_number(2)
obj.findMedian()