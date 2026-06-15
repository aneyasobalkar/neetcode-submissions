class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        n = len(matrix)
        middle_row_index = n // 2
        middle_row = matrix[middle_row_index]
        if target in middle_row:
            return True
        if target < middle_row[0]:
            return self.searchMatrix(matrix[:middle_row_index], target)
        else:
            return self.searchMatrix(matrix[middle_row_index+1:], target)
