import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        min_heap = [(0, k)]
        visited = set()
        travel_time = 0
        
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visited:
                continue
            visited.add(n1)
            travel_time = max(travel_time, w1)
            
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, (w1 + w2, n2))
                    
        return travel_time if len(visited) == n else -1
