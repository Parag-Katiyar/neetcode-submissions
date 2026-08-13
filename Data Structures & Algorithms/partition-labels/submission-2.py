from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l = len(s)
        hmap = {}
        
        # Step 1: Populate intervals [start, end] for each character
        for i in range(0, l):
            if s[i] in hmap:
                hmap[s[i]][1] = i
            else:
                hmap[s[i]] = [i, i]
                
        curr_start = 0
        curr_end = 0
        count = 0
        result = []
        
        # Step 2: Merge overlapping intervals
        for i in hmap:
            if count == 0:
                curr_start = hmap[i][0]
                curr_end = hmap[i][1]
                count = 1
                continue
            
            # CONDITION 1: The new interval is completely inside the current window
            #if hmap[i][0] <= curr_end and hmap[i][1] <= curr_end:
            #    continue  # Do nothing, it's safely contained
                
            # CONDITION 2: The new interval starts inside, but extends past the end
            elif hmap[i][0] <= curr_end and hmap[i][1] > curr_end:
                curr_end = hmap[i][1]  # Extend your current window
                
            # CONDITION 3: The new interval starts after the current window ends
            elif hmap[i][0] > curr_end:
                result.append(curr_end - curr_start + 1)  # Save the finished partition
                curr_start = hmap[i][0]                   # Start a brand new window
                curr_end = hmap[i][1]
                
        # Append the final remaining partition after the loop finishes
        result.append(curr_end - curr_start + 1)
        return result