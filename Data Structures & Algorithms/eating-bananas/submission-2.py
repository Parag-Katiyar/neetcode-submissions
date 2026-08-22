class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

        time = 0 
        ans = 0 
        
        middle = (start + end)//2
         
        while start <=end : 

            #middle = (start + end)//2
            time = 0 

            for i in range(0,len(piles)):

                if piles[i]%middle != 0: 
                    time = time + (piles[i]//middle) + 1
                else: 
                    time = time + (piles[i]//middle)

            if time - h > 0:
                start = middle+1
                middle = (start + end)//2
                
                
            elif time - h <= 0: 
                ans = middle
                end = middle-1
                middle = (start + end)//2
                
                

        return ans


            