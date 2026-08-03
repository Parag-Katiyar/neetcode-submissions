class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area1 = 0 
        area2 = 0
        a = 0
        l = 0 
        r = len(heights)- 1

        area1 = (min(heights[l], heights[r]))*(r - l)
        a = area1 


        while l<r:

            areacur = (min(heights[l], heights[r]))*(r - l)

            if a < areacur: 
                a = areacur

        
            
            area2 = (min(heights[l+1], heights[r]))*(r - l-1)
            area3 = (min(heights[l], heights[r-1]))*(r- 1 - l)

            if area2 > a and area2> area3 and l<r: 
                l = l+1 
                a = area2
                continue

            if area3 > a and area3 > area2 and l<r:
                r = r -1 
                a = area3
                continue

            else:
                if l<r:
                   if heights[l] < heights[r]:
                    l = l + 1
                   else:
                    r = r - 1
        return a 












        