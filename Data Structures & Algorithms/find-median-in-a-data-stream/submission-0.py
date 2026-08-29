import heapq
class MedianFinder:

    def __init__(self):
        self.max_bottom = []
        self.min_top = []
        

    def addNum(self, num: int) -> None:

        l_top = len(self.min_top)
        l_bottom = len(self.max_bottom) 

        if l_top == 0:
            heapq.heappush(self.min_top, num) 

        elif num < self.min_top[0]:
            x = -1*num 
            heapq.heappush(self.max_bottom, x)

        else: 
            heapq.heappush(self.min_top, num)
        
        l_top = len(self.min_top)
        l_bottom = len(self.max_bottom)
        total_len = l_top + l_bottom 

        #odd 

        if total_len%2 == 1:

            if l_top > l_bottom + 1 : 

                x = heapq.heappop(self.min_top)
                x = -1*x
                heapq.heappush(self.max_bottom, x)

                l_top = l_top - 1 
                l_bottom = l_bottom + 1


            elif l_top <= l_bottom:
                    
                x = heapq.heappop(self.max_bottom)
                x = -1*x
                heapq.heappush(self.min_top, x)

                l_top = l_top + 1 
                l_bottom = l_bottom - 1

                    
        #even

        elif total_len%2 == 0:


            if l_top > l_bottom: 

                x = heapq.heappop(self.min_top)
                x = -1*x
                heapq.heappush(self.max_bottom, x)

                l_top = l_top - 1 
                l_bottom = l_bottom + 1
                    
            elif l_top < l_bottom:

                x = heapq.heappop(self.max_bottom)
                x = -1*x
                heapq.heappush(self.min_top, x)

                l_top = l_top + 1 
                l_bottom = l_bottom - 1

        

        #median = top_heap[0]
        #median = (top_heap[0] + bottom_heap[0])//2

    def findMedian(self) -> float:

        total_len = len(self.min_top) + len(self.max_bottom)

        if total_len == 0:
            return 0.0
        

        if total_len%2 == 0: 
            return (self.min_top[0] - self.max_bottom[0])/2
        else:
            return self.min_top[0]














        
        