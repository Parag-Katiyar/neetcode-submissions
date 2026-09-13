##### Krushal #####

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        all_distance = []
        l = len(points)
        count = 0 
        cost = 0 

        for i in range (0,l): 

            for j in range(i+1,l):

                cuur_distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

                all_distance.append([cuur_distance,tuple(points[j]),tuple(points[i])])
            
        all_distance.sort()

        parents = {}

        for point in points:
            p = tuple(point)
            parents[p] = p

        def find(p):

            p = tuple(p)

            if parents[p] == p:
                return p

            parents[p] = find(parents[p])

            return parents[p]


        def union(root_1, root_2):

            if root_1 == root_2: 
                return -1
            else: 
                #root_2-->root_1
                parents[root_2] = root_1
                return 1 
            #one optimisation is missing of which one is bigger join that tree

        
        i = 0 

        while count < l-1: 

            root_1 = find(all_distance[i][1])
            root_2 = find(all_distance[i][2])

            if union(root_1,root_2) == 1:
                count = count + 1 
                cost = cost + all_distance[i][0]
                i = i + 1
            else: 
                i = i + 1
                continue
        
        return cost

    
                



             