class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False
        
        i, m = 0, len(matrix)
        j = len(matrix[0]) - 1
        
        
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            else:
                if matrix[i][j] > target:
                    j -= 1
                else:
                    i += 1
            
        return False