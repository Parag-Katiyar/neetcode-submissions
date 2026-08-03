def trav(node, local, full_set, graph):

    # Already completely processed
    if node in full_set:
        return True

    # Cycle found
    if node in local:
        return False

    # Add current node to current path
    local.add(node)

    # graph.get(node, []) handles nodes with no outgoing edges
    for k in graph.get(node, []):

        # If any neighbour has a cycle, stop immediately
        if not trav(k, local, full_set, graph):
            return False

    # Finished exploring this node
    local.remove(node)
    full_set.add(node)

    return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {}

        for a, b in prerequisites:
            graph.setdefault(b, []).append(a)

        full_set = set()

        # Check every course (graph may be disconnected)
        for i in range(numCourses):

            if not trav(i, set(), full_set, graph):
                return False

        return True
        