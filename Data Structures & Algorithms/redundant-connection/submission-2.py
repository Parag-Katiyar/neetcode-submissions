#The key sentence to remember:

#Only when two trees of equal rank are joined does the new root's rank increase.

#And one subtle point: with union by rank, rank is a bound/measure related to tree height; after path compression, it isn't necessarily the exact current height.

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

      n = len(edges)

      parent = list(range(n+1))
      rank =  [1] * (n + 1)

      def find(edge_1,): 

        if parent[edge_1] == edge_1: 
          return edge_1

        parent[edge_1] = find(parent[edge_1])

        return parent[edge_1]

      def union(r1,r2):

        if r1 == r2: 
          return 1 

        if rank[r1] < rank[r2]:
          parent[r1] = r2

        elif rank[r1] > rank[r2]:
          parent[r2] = r1

        else:
          parent[r2] = r1
          rank[r1] += 1
        
        return 0 

        #if r1 == r2:
        #  return 1

        #elif r1 != r2: 
        #  parent[r2] = r1

        #return 0 
      

      for i in range(0,n):

        #edges[0], edges[1]

        root_1 = find(edges[i][0])
        root_2 = find(edges[i][1])

        if union(root_1, root_2) == 1: 
          return edges[i]



        