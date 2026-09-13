import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        all_distance = []
        l = len(points)
        count = 0
        cost = 0

        # Generate all edges
        for i in range(l):
            for j in range(i + 1, l):

                curr_distance = (
                    abs(points[i][0] - points[j][0])
                    + abs(points[i][1] - points[j][1])
                )

                all_distance.append(
                    [curr_distance, tuple(points[j]), tuple(points[i])]
                )

        # Cheapest edges first
        all_distance.sort()

        # DSU
        parent = {}

        for point in points:
            p = tuple(point)
            parent[p] = p

        def find(p):

            p = tuple(p)

            if parent[p] == p:
                return p

            parent[p] = find(parent[p])

            return parent[p]

        def union(root_1, root_2):

            if root_1 == root_2:
                return -1

            # root_2 → root_1
            parent[root_2] = root_1

            return 1

        # Kruskal
        i = 0

        while count < l - 1:

            root_1 = find(all_distance[i][1])
            root_2 = find(all_distance[i][2])

            if union(root_1, root_2) == 1:
                count += 1
                cost += all_distance[i][0]

            i += 1

        return cost