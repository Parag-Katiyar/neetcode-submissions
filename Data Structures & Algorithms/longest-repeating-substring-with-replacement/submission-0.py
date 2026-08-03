class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        unique_characters = set(s)
        max_length = 0
        
        for target in unique_characters:
            left = 0
            non_target_count = 0

            for right in range(len(s)):

                if s[right] != target:
                    non_target_count += 1

                while non_target_count > k:

                    if s[left] != target:
                        non_target_count -= 1
                        
                    left += 1

                max_length = max(max_length, right - left + 1)

        return max_length

