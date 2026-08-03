def traverse(node, parent, graph, visited):

    if node in visited: 
        return False

    visited.add(node)

    for i in graph.get(node, []): 

        if i != parent: 
            if traverse(i, node, graph, visited) == False : 
                return False

    return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {}
        l = len(edges)

        for i in range(0, l): 
            
            graph.setdefault(edges[i][1],[]).append(edges[i][0])
            graph.setdefault(edges[i][0],[]).append(edges[i][1])

        visited = set()


        if traverse(0, -1, graph, visited) == False or len(visited) != n: 
            return False 
        else: 
            return True
        











