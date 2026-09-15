# Is this greedy?
# Id phrase it like this:
# The algorithm has a greedy selection step, but the deeper idea is the same Dijkstra framework.

# The greedy part is:

# Always process the currently reachable state with the smallest required water level first.

#So dont think:
#"Greedy because 5 is the best and therefore always globally best."
#Think:
#"Among everything currently reachable, 5 is the smallest required water level, so let's expand it first."

#That's the Dijkstra connection.

import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        heap_one = []
        r = len(grid) 
        c = len(grid[0])

        setx = set()

        heapq.heappush(heap_one, (grid[0][0],0,0))


        while heap_one: 

            val,x,y = heapq.heappop(heap_one)

            if (x,y) in setx: 
                continue
            else: 
                setx.add((x,y))

            if x == r-1 and y == c-1:
                return val

            if 0 <= x+1 <= r-1:
                if val > grid[x+1][y]: 
                    heapq.heappush(heap_one, (val,x+1,y))
                    
                else: 
                    heapq.heappush(heap_one, (grid[x+1][y],x+1,y))

            if 0 <= x-1 <= r-1:
                if val > grid[x-1][y]: 
                    heapq.heappush(heap_one, (val,x-1,y))
                else: 
                    heapq.heappush(heap_one, (grid[x-1][y],x-1,y))

            if 0 <= y+1 <= c-1:
                if val > grid[x][y+1]: 
                    heapq.heappush(heap_one, (val,x,y+1))
                else: 
                    heapq.heappush(heap_one, (grid[x][y+1],x,y+1))

            if 0 <= y-1 <= c-1:
                if val > grid[x][y-1]: 
                    heapq.heappush(heap_one, (val,x,y-1))
                else: 
                    heapq.heappush(heap_one, (grid[x][y-1],x,y-1))
            



























        