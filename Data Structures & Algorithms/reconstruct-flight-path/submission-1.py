class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        mapx = {}

        for i in tickets:
            if i[0] not in mapx: 
                mapx[i[0]] = []
                mapx[i[0]].append(i[1])
            else: 
                mapx[i[0]].append(i[1])
        
        for x in mapx:
            mapx[x].sort(reverse=True)
            
        stack = ["JFK"]
        answer = []


        while stack:

            if mapx.get(stack[-1],[]):

                x = mapx[stack[-1]].pop()
                stack.append(x)

            else: 
                ans = stack.pop()
                answer.append(ans)

        answer.reverse()
        return answer








        
            