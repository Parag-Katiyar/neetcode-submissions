#Clener Version# 

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def num(i):
            if i == n:
                return 1

            if s[i] == '0':
                return 0

            if i in memo:
                return memo[i]

            ways = num(i + 1)

            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                ways += num(i + 2)

            memo[i] = ways
            return ways

        return num(0)