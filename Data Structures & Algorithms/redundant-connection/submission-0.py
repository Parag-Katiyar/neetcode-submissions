class Solution:

  def findParent(self, parent, i):
    if parent[i] == i:
      return i
    parent[i] = self.findParent(parent, parent[i])
    return parent[i]

  def union(self, parent, rank, x, y):
    rootX = self.findParent(parent, x)
    rootY = self.findParent(parent, y)

    if rootX != rootY:
      if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
      elif rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
      else:
        parent[rootY] = rootX
        rank[rootX] += 1
      return True
    return False

  def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
    parent = list(range(len(edges) + 1))
    rank = [1] * (len(edges) + 1)

    for u, v in edges:
      if not self.union(parent, rank, u, v):
        return [u, v]
    return []

        