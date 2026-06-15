class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def neighbors(x, y):
            arr = []
            if x - 1 >= 0:
                arr.append((x-1, y))
            if x + 1 < len(board[0]) :
                arr.append((x+1, y))
            if y - 1 >= 0:
                arr.append((x, y-1))
            if y + 1 < len(board):
                arr.append((x, y+1))
            return arr

        def dfs(x, y, visited):
            visited.add((x, y))
            for n_x, n_y in neighbors(x, y):
                if board[n_y][n_x] == "O" and (n_x, n_y) not in visited:
                    if (n_y ==0 or n_x == 0 or n_y == (len(board) -1) or n_x == (len(board[0]) - 1)):
                        nonlocal contains_o_on_edge
                        contains_o_on_edge = True
                        return
                    dfs(n_x, n_y, visited)

        ROWS, COLS = len(board), len(board[0])
        for r in range(1, ROWS-1):
            for c in range(1,  COLS-1):
                if board[r][c] == "O":
                    contains_o_on_edge = False
                    region = set()
                    dfs(c,r, region)
                    if not contains_o_on_edge:
                        for rx, ry in region:
                            board[ry][rx] = "X"


