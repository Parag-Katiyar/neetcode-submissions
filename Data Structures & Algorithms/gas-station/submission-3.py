class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        l = len(gas)
    
        sumx = 0
        start = 0

        i = 0 

        if sum(gas) - sum(cost) < 0:
            return -1
        
        real_start = 0
        
        while i < l: 

            sumx = sumx + gas[i] - cost[i]

            if sumx < 0:
                start = i + 1
                sumx = 0  

            i = i + 1

        return start 