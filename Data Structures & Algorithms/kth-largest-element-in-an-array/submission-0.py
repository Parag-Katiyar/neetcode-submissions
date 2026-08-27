import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap1 = []

        for i in range(0,len(nums)): 

            if len(heap1) < k: 
                
                heapq.heappush(heap1, nums[i])
            else: 
                if heap1[0] <nums[i]: 
                    heapq.heapreplace(heap1, nums[i])
                
        return heap1[0]
                    
                
