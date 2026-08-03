class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        final = [target - pos for pos in position]

        com = [[final[i], speed[i]] for i in range(len(final))]

        com.sort(key=lambda x: x)

        l = len(final)

        t = []

        for i in range(0,l): 

            t.append(com[i][0]/com[i][1])

        if not t: 
            return 0

       
        fleet = t[0]

        i = 1
        count = 1

        

        while i < l:

            if t[i] > fleet:
                count += 1
                fleet = t[i]

            i = i + 1 
        
        return count 



