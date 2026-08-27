
#Because there is a comma between the formula -1*(x*x + y*y) and the coordinate list [x,y], Python thinks you are trying to pass two separate things into .append().To fix it, you just need to wrap the whole thing in an extra set of square brackets [...] so Python treats it as one single list item.

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dis = []
        
        for i in range(0,len(points)): 

            x = points[i][0]*points[i][0]
            y = points[i][1]*points[i][1]

            z = -1*( x + y )

            dis.append([z,[points[i][0],points[i][1]]])

        heap1 = []

        for i in range(0,len(points)): 

            if len(heap1)<k: 
                heapq.heappush(heap1, dis[i])
            else: 
                if heap1[0] < dis[i]: 
                    heapq.heapreplace(heap1, dis[i])
                #if heap1[0] == dis[i]:
                #    heapq.heappush(heap1, dis[i]) 
        
        return [item[1] for item in heap1]
                    




        

        
            