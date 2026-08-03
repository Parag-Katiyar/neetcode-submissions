class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        store = [0]*k

        t = 0

        for i in nums:
            d[i] = d.get(i,0) + 1

        for j in d:

            if t < k:

                store[t] = j

                t = t +1 
            
            else:

                min_index = min(range(len(store)), key=lambda i: d[store[i]])

                if  d[j] > d[store[min_index]]:

                    

                    store[min_index] = j

        
        return(store)
            





        