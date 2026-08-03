def traverse(node, parent, varified, graph): 

    if node in varified:
        return
    
    varified.add(node)

    for i in graph.get(node, []): 

        if i != parent: 
            traverse(i, node, varified, graph)

    return 
                



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = {}
        count = 0 

        for i in range(0,n):
            graph[i] = []

        l = len(edges)

        for i in range(0, l): 
            
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])

        visited = set()
        
        for i in graph: 

            if i not in visited:

                traverse(i,-1,visited, graph)

                if len(visited) == n: 
                    return count + 1

                if len(visited) !=n: 
                    count = count + 1
            
        return count

        









