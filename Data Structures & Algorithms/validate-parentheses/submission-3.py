class Solution:
    def isValid(self, s: str) -> bool:

        s = list(s)
        s2 = []

        while s:

            s2.append(s.pop())

            while (
                s and s2 and
                (
                    (s[-1] == '(' and s2[-1] == ')') or
                    (s[-1] == '[' and s2[-1] == ']') or
                    (s[-1] == '{' and s2[-1] == '}')
                )
            ):
                s.pop()
                s2.pop()

        return not s and not s2




        