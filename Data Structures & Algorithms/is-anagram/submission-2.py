class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = {}
        seen2 = {}

        if len(s) != len(t):
            return False 

        for i in s:
            if i not in seen1:
                seen1[i] = 1

            if i in seen1:
                seen1[i] = seen1[i] + 1

        for j in t:
            if j not in seen2:
                seen2[j] = 1

            if j in seen2:
                seen2[j] = seen2[j] + 1


        if seen1 == seen2:
            return True 
            
        if seen1 != seen2:
            return False
        

        