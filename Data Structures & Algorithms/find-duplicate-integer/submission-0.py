# Values in 1..n -------→ try using the value as an index.
# Cycle ---------→ use slow/fast pointers.

# What you hadn't yet connected was:

# "These array-index jumps can themselves create a linked-list-like cycle."

# That's the kind of connection that only really comes from seeing enough problems.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        fast = nums[0]

        # Phase 1: find intersection inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2: find entrance of the cycle
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
        