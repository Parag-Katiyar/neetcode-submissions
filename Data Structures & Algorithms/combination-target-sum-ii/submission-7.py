class Solution:
    def combinationSum2(self, candidates: List[int], target: int):
        candidates.sort()
        ans = []

        def backtrack(start, curr, total):
            if total == target:
                ans.append(curr[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                curr.append(candidates[i])
                backtrack(i + 1, curr, total + candidates[i])  # i+1 because each number is used once
                curr.pop()

        backtrack(0, [], 0)
        return ans