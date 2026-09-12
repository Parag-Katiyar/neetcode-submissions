import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        min_heap = [(0, 0)]  # Stores tuples of (cost, point_index)
        visited = set()
        total_cost = 0
        
        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)
            
            # If the point is already in our MST, skip it
            if i in visited:
                continue
                
            # Include this point in our MST
            visited.add(i)
            total_cost += cost
            
            # Calculate Manhattan distances to all unvisited neighbors
            x1, y1 = points[i]
            for j in range(n):
                if j not in visited:
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (dist, j))
                    
        return total_cost
