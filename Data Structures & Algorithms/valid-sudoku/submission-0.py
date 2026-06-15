class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for item in row:
                if item in seen:
                    return False
                else:
                    if item != ".":
                        seen.add(item)
        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j] in seen:
                    return False
                elif board[i][j] != ".":
                    seen.add(board[i][j])
        
        row_set = []
        for row_index in [3,6,9]:
            kernel = board[row_index-3: row_index]
            for col_index in [3,6,9]:
                flattened_board = []
                for row in kernel:
                    flattened_board.extend(row[col_index-3:col_index])
                row_set.append(flattened_board)

        for row in row_set:
            seen = set()
            for item in row:
                if item in seen:
                    return False
                else:
                    if item != ".":
                        seen.add(item)

        return True