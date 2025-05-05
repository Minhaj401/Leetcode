class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """  
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        smallest = min(nums)
        largest = max(nums)
        return gcd(smallest, largest)