class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = set()
        countmax = 0
        left = 0  # Tracks the start of the current unique window

        for i in range(len(s)):
            while s[i] in x:
                x.remove(s[left])
                left += 1

            x.add(s[i])
            count = i - left + 1

            if count > countmax:
                countmax = count

        return countmax





        