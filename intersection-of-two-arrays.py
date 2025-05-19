class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a,b=set(nums1),set(nums2)
        return list(i for i in a if i in b)