class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = [[] for _ in range(n)]
        dist = [[float("inf")] * (k + 2) for _ in range(n)]

        for u, v, price in flights:
            adj[u].append((v, price))

        dist[src][0] = 0
        heap = [(0, src, 0)]   # cost, node, flights_used

        while heap:
            cost, node, flights_used = heapq.heappop(heap)

            if node == dst:
                return cost

            if flights_used == k + 1:
                continue

            for nei, price in adj[node]:
                new_cost = cost + price
                new_flights = flights_used + 1

                if new_cost < dist[nei][new_flights]:
                    dist[nei][new_flights] = new_cost
                    heapq.heappush(
                        heap, (new_cost, nei, new_flights)
                    )

        return -1