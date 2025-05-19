class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        return float(sum(sorted(salary)[1:-1]))/float(len(salary)-2)