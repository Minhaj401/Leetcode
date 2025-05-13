class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        a=[]
        for i in arr:
            if i==arr.count(i):
                a.append(i)
        if len(a)==0:
            return -1
        return max(set(a))
        