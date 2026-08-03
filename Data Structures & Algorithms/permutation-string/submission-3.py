class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

   
        char_counts = [0] * 26
        for i in range(len1):
            char_counts[ord(s1[i]) - ord('a')] += 1

        left = 0

        for right in range(len2):
            right_idx = ord(s2[right]) - ord('a')
            char_counts[right_idx] -= 1  
            while char_counts[right_idx] < 0:
                left_idx = ord(s2[left]) - ord('a')
                char_counts[left_idx] += 1  
                left += 1

            if (right - left + 1) == len1:
                return True

        return False
        