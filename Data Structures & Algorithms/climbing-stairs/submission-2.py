class Solution:
    def climbStairs(self, n: int) -> int:
        collections = {1:1, 2:2}

        def count(n): 
            if n in collections: 
                return collections[n]
            
            count_n = count(n-1) + count(n-2)
            collections[n] = count_n

            return count_n
        
        return count(n)

    
    
        


        