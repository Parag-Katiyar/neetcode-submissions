from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)
        cols = len(grid[0])

        que = deque()

        # Put all treasures into the queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    que.append((i, j))

        directions = [
            (1, 0),   # down
            (-1, 0),  # up
            (0, 1),   # right
            (0, -1)   # left
        ]

        while que:

            x, y = que.popleft()

            for dx, dy in directions:

                nx = x + dx
                ny = y + dy

                if 0 <= nx < rows and 0 <= ny < cols:

                    if grid[nx][ny] == 2147483647:

                        grid[nx][ny] = grid[x][y] + 1
                        que.append((nx, ny))