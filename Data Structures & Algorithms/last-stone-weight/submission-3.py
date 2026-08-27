import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if len(stones) == 1: 
            return stones[0]

        stones = [-x for x in stones]

        heapq.heapify(stones)

        while len(stones) > 1:

            x1 = heapq.heappop(stones)
            x2 = heapq.heappop(stones)
        
            if x1 != x2:
                heapq.heappush(stones, x1-x2)

            if len(stones) == 1:
                return -1*stones[0]

            if len(stones) == 0: 
                return 0



 