from typing import List

class CountSquares:

    def __init__(self):
        # Maps (x, y) tuple -> frequency count
        self.points = {}

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] = self.points.get((x, y), 0) + 1

    def count(self, point: List[int]) -> int:
        qx, qy = point
        ans = 0

        # Loop through all unique points to find diagonal opposites
        for (x, y), freq in self.points.items():
            # Must be strictly diagonal (cannot be on the same horizontal or vertical line)
            if qx == x or qy == y:
                continue

            # Check if horizontal distance equals vertical distance
            if abs(qx - x) == abs(qy - y):
                # The remaining two corners required to form the square
                p1 = (x, qy)
                p2 = (qx, y)

                # Multiply counts of the 3 corners and add to total combinations
                ans += freq * self.points.get(p1, 0) * self.points.get(p2, 0)

        return ans
