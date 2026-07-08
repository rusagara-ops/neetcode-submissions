class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."]*n for _ in range(n)]


        cols = set()
        posdiagonals = set() #(r+)
        negdiagonals = set() #(r-c)

        def backtrack (r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)

            for c in range(n):
                if c in cols or (r+c) in posdiagonals or (r-c) in negdiagonals:
                    continue

                cols.add(c)
                posdiagonals.add(r+c)
                negdiagonals.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                cols.remove(c)
                posdiagonals.remove(r+c)
                negdiagonals.remove(r-c)
                board[r][c] = "."

        backtrack(0)

        return result





