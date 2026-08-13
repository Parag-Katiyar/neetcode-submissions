class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        l = len(s)
        hmap = {}
        
        for i in range(0,l):

            if s[i] in hmap:
                hmap[s[i]][1] = i
                    
            if s[i] not in hmap: 
                hmap[s[i]] = [i,i]
                

        curr_start = 0 
        curr_end = 0
        count = 0
        result = [] 

        
        for i in hmap: 

            if count == 0: 
                curr_start = hmap[i][0] 
                curr_end = hmap[i][1]
                count = 1
                continue

            if hmap[i][0] <= curr_end and hmap[i][1] > curr_end:
                curr_end = hmap[i][1]
                

            elif hmap[i][0]> curr_end:
                result.append(curr_end - curr_start + 1)
                
                curr_start = hmap[i][0]
                curr_end = hmap[i][1]

        result.append(curr_end - curr_start + 1)

        return result















