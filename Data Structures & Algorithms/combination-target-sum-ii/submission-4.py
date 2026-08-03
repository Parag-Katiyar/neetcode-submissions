class Solution:

  def combinationSum2(
      self, candidates: List[int], target: int
  ) -> List[List[int]]:
    ans = []
    state = []

    # 'blocked' tracks numbers completely finished at higher levels
    def backtrack(start, total, blocked):
      if total == target:
        ans.append(state[:])
        return
      if total > target:
        return

      # Tracks numbers used as a parent at THIS specific loop level
      level_parents = set()

      for i in range(start, len(candidates)):
        num = candidates[i]

        # 1. Skip if blocked by an older ancestor branch
        # 2. Skip if we already used it as a parent at this level
        if num in blocked or num in level_parents:
          continue

        level_parents.add(num)

        # Process the first duplicate normally
        state.append(num)
        backtrack(i + 1, total + num, blocked)
        state.pop()

        # YOUR LOGIC: After the first duplicate's recursion finishes completely,
        # we block it so it cannot appear in any future sibling/child branches.
        # We pass a new copy of the set to avoid cross-contaminating parallel branches.
        blocked = blocked | {num}

    backtrack(0, 0, set())
    return ans