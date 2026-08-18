class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] = self.points.get((x, y), 0) + 1

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0

        for (x2, y2), freq in self.points.items():

            if x2 != x or y2 == y:
                continue

            d = y2 - y

            ans += freq * self.points.get((x + d, y), 0) \
                        * self.points.get((x + d, y2), 0)

            ans += freq * self.points.get((x - d, y), 0) \
                        * self.points.get((x - d, y2), 0)

        return ans
        



