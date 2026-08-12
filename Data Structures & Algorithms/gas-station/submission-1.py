class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        l = len(gas)

        net = [0]*l
        
        for i in range(0,l):
            net[i] = gas[i] - cost[i]
        
        sumx = 0
        start = 0

        i = 0 

        if sum(net) < 0:
            return -1
        
        real_start = 0
        
        while i < l: 

            sumx = sumx + net[i]

            if sumx < 0:
                start = i + 1
                real_start = i + 1
                sumx = 0  

            i = i + 1

        return real_start 




        
         
