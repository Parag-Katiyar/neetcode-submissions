from collections import deque
class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Making list ! 
        mapx = {}
        countp = {}
        remaining = numCourses


        for i in range(0,numCourses): 
            mapx[i] = []
            countp[i] = 0 

        for j in prerequisites: 

            i = 0
            l = len(j)

            for i in range(0,l-1):

                mapx[j[i+1]].append(j[i]) #outgoing
                countp[j[i]] = countp[j[i]] + 1 #incoming

        que = deque()
        result = []

        for i in countp: 
            if countp[i] == 0:
                que.append(i)
                remaining = remaining - 1 


        while que:

            node = que.popleft()
            result.append(node)

            for i in mapx[node]: 

                if countp[i] != 0:

                    countp[i] = countp[i] - 1

                    if countp[i] == 0: 
                        que.append(i)
                        remaining = remaining -1 

        
        
        if remaining !=0: 
            return []
        if remaining == 0: 
            return result

            

            
                            



        
        
            


                




