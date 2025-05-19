class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        a=zip(heights,names)
        a.sort(reverse=True, key=lambda x: x[0])
        sorted_names = [name for height, name in a]
        return sorted_names
