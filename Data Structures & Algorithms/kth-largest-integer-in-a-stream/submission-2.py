import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.heap1 = []
        #self.nums = nums

        i = 0 

        while i < len(nums): 

            if i < k: 
                heapq.heappush(self.heap1, nums[i])
                i = i + 1
                
            elif i >= k: 
                if nums[i] > self.heap1[0]:
                    heapq.heapreplace(self.heap1, nums[i])
                i = i + 1


    def add(self, val: int) -> int:

        if len(self.heap1) == 0: 
            heapq.heappush(self.heap1, val)
            return val

        if len(self.heap1) <= self.k-1: 
            heapq.heappush(self.heap1,val)
            return self.heap1[0]

#If the lenght is less then the k then we have to return the smallest of them !!

        if val > self.heap1[0]:
                    heapq.heapreplace(self.heap1, val)
        return self.heap1[0]


        




        









