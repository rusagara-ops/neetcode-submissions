class Solution:
    def solve(self, board: List[List[str]]) -> None:
        cols = len(board[0])
        rows = len(board)

        def capture(r,c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r+1,c)
            capture(r,c+1)
            capture(r-1,c)
            capture(r, c-1)

        # capture all the cells on the edge and find the unsorrounded regions O to T
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and (r in [0,rows-1] or c in [0, cols-1])):
                    board[r][c] = "T"
                    capture(r,c)
        # changes the middle surrounded regions O to X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                

        # uncapture the unsurrounded regions
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
