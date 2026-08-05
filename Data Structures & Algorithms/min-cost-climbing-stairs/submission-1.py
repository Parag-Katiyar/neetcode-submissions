class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {0:0, 1:0}

        def min_cost(i): 

            if i in memo: 
                return memo[i]
            
            min_i = min((min_cost(i-1) + cost[i-1]) , (min_cost(i-2)+cost[i-2]))

            memo[i] = min_i

            return min_i
        
        n = len(cost)
        
        return min_cost(n) 
        