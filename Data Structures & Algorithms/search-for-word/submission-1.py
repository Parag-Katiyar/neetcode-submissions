class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1)    # right
        ]

        def dfs(r, c, index):

            # Whole word matched
            if index == len(word):
                return True

            # Boundary check
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # Character does not match
            if board[r][c] != word[index]:
                return False

            # Mark visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore all directions
            for dr, dc in directions:
                if dfs(r + dr, c + dc, index + 1):
                    board[r][c] = temp   # restore
                    return True

            # Undo change (backtracking)
            board[r][c] = temp

            return False


        for i in range(rows):
            for j in range(cols):

                if dfs(i, j, 0):
                    return True

        return False