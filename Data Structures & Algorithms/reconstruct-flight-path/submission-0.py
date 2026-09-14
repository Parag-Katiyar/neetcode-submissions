from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # Sort tickets in reverse lexical order so we can pop the smallest efficiently
        tickets.sort(reverse=True)
        
        graph = defaultdict(list)
        for frm, to in tickets:
            graph[frm].append(to)
            
        res = []
        def dfs(airport: str):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            res.append(airport)
            
        dfs("JFK")
        return res[::-1]
