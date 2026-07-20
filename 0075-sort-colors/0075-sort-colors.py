class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        b = 0
        c = 0

        for i in nums:
            if i == 0:
                a += 1
            elif i == 1:
                b += 1
            else:
                c += 1

        s = 0

        for i in range(a):
            nums[s] = 0
            s += 1

        for i in range(b):
            nums[s] = 1
            s += 1

        for i in range(c):
            nums[s] = 2
            s += 1            
