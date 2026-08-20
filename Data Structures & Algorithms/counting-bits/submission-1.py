class Solution:

  def countBits(self, n: int) -> List[int]:
    dp = [0] * (n + 1)

    for i in range(n + 1):
      # PUSH forward to 2 * i (left shift by 1, +0 bit)
      if 2 * i <= n:
        dp[2 * i] = dp[i]

      # PUSH forward to 2 * i + 1 (left shift by 1, +1 bit)
      if 2 * i + 1 <= n:
        dp[2 * i + 1] = dp[i] + 1

    return dp