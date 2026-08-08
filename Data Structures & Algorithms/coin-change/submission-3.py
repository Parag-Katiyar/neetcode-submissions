class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        
        def mcoin(i,amount):

            if amount ==0: 
                return 0

            if i < 0 or amount < 0: 
                return -1
            
            if (i, amount) in memo:
                return memo[(i, amount)]

            min_j = []

            for j in range(0, int(amount/coins[i])+1): 

                count_j = mcoin(i-1,amount - coins[i]*j)
    
    
                if  count_j != -1:
                    min_j.append(j + count_j)
            
            

            if min_j: 
                memo[(i, amount)] = min(min_j)
                return min(min_j)
            else: 
                memo[(i, amount)] = -1
                return -1
                
            
            
        return mcoin(len(coins)-1,amount)



