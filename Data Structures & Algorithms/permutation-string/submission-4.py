class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        target_mp = {}
        for char in s1:
            target_mp[char] = target_mp.get(char, 0) + 1

        allowed_chars = set(s1) 

        current_mp = {}
        left = 0

        for right in range(len(s2)):
            char = s2[right]
            if char not in allowed_chars:
                current_mp.clear()
                left = right + 1
                continue
            current_mp[char] = current_mp.get(char, 0) + 1

            while current_mp[char] > target_mp[char]:
                left_char = s2[left]
                current_mp[left_char] -= 1
                left += 1
            
       
            if (right - left + 1) == len(s1):
                return True
   
        return False
        
