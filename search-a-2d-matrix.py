class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        flag=False
        for i in matrix:
            if target in i:
                flag=True
        return flag