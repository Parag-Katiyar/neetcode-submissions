class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        current_partition = []
        
        def is_palindrome(sub_str: str) -> bool:
            return sub_str == sub_str[::-1]
        
        def backtrack(start_index: int):
            # Base Case: If we reach the end of the string, save the path
            if start_index >= len(s):
                result.append(list(current_partition))
                return
            
            # Explore all prefixes starting from start_index
            for end_index in range(start_index + 1, len(s) + 1):
                substring = s[start_index:end_index]
                
                if is_palindrome(substring):
                    current_partition.append(substring) # Choose
                    backtrack(end_index)                # Explore
                    current_partition.pop()             # Backtrack

        backtrack(0)
        return result

# How to run it:
# solver = Solution()
# print(solver.partition("aab"))
