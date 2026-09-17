class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        return len([i for i in (range(len(heights))) if heights[i]!=sorted(heights)[i]])