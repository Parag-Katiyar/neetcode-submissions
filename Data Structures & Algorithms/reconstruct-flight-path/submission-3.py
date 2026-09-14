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
        #for x in mapx: ### SYNTAX ####
        #    mapx[x].sort()
        #    mapx[x].reverse()
            
        stack = ["JFK"]
        answer = []


        while stack:

            if mapx.get(stack[-1],[]): ### SYNTAX and .get !!!!!

                x = mapx[stack[-1]].pop()
                stack.append(x)

            else: 
                ans = stack.pop()
                answer.append(ans)

        answer.reverse() # Syantax !!!!!! 
        return answer
   