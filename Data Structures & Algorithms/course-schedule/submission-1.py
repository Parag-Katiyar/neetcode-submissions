def trav(node,full_set,local_set,graph): 

    if node in full_set: 
        return True 

    if node in local_set: 
        return False 
    
    local_set.add(node)


    for k in graph.get(node, []):

        if k in local_set:
            return False

        if trav(k,full_set,local_set,graph) == False: 
            return False 

    local_set.remove(node)
    full_set.add(node)

    return True 


        

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        l = len(prerequisites)

        for i in range(0, l): 
            
            graph.setdefault(prerequisites[i][1],[]).append(prerequisites[i][0])
        
        # Traverse 

        full_set = set()

        for i in graph:

            local_set = set()

            if trav(i,full_set,local_set,graph) == False: 
                return False

        return True


        


        
        