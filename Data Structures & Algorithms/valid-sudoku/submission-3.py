class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_map = {}
        #look through rows
        for row in board:
            board_map = Counter(row)
            if "." in board_map:
                del board_map["."]
            for key in board_map:
                if board_map[key] > 1:
                    return False
        for col in range(9): 
            board_map = {}
            for row in range(9):
                val = board[row][col]
                if val != ".":
                    board_map[val] = board_map.get(val, 0) + 1
            for key in board_map:
                if board_map[key] > 1:
                    return False
        for row in [3, 6, 9]:
            board_subset = board[row - 3:row]
            for x in [3,6,9]:
                board_map = {}
                for b in board_subset:
                    b_prime = b[x-3:x]
                    for val in b_prime:
                        if val != ".":
                            board_map[val] = board_map.get(val, 0) + 1
                for key in board_map:
                    if board_map[key] > 1:
                        return False

        return True