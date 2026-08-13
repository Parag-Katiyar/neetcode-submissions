class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        l = len(triplets)
        check = [0,0,0]
      

        for i in range(0,l): 

            if (triplets[i][0] <= target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]):


                if triplets[i][0] == target[0]:
                    check[0] = 1

                if triplets[i][1] == target[1]:
                    check[1] = 1

                if triplets[i][2] == target[2]:
                    check[2] = 1
        
        
        if check == [1,1,1]: 
            return True  
                
        return False
               



            
