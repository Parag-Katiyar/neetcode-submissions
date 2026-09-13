###   Prim   ###
import heapq

def dis(point_1, point_2):

     m_dis =  abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])

     return (m_dis,point_1,point_2)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        heap_one = []
        visited = set()
        count = 1 
        cost = 0 
        l = len(points)


        def connections(point): 
            for i in points:

                if tuple(i) in visited:
                    continue

                heapq.heappush(heap_one, dis(i,point))

        visited.add(tuple(points[0]))
        connections(points[0])

        while count < l: 

            x = heapq.heappop(heap_one)

            if tuple(x[1]) in visited: 
                continue
            else: 
                count = count + 1
                cost = cost + x[0]

                visited.add(tuple(x[1]))

                connections(x[1])
            
        return cost







        








