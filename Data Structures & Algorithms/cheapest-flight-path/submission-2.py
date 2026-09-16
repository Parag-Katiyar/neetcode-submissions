class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        INF = float("inf")
        dist = [INF] * n
        dist[src] = 0

        # k stops = k + 1 flights maximum
        for _ in range(k + 1):
            old = dist.copy()

            for u, v, price in flights:
                if old[u] != INF:
                    dist[v] = min(dist[v], old[u] + price)

        return -1 if dist[dst] == INF else dist[dst]