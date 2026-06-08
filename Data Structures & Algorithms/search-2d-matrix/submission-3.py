class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        l = 0
        r = row*col-1

        while l <= r:
            mid = (l+r)//2
            a, b = divmod(mid, col)
            if matrix[a][b] == target:
                return True
            elif matrix[a][b] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False