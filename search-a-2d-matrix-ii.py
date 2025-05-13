class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        found=0
        for i in matrix:
            for j in i:
                if j==target:
                    return True
        return False