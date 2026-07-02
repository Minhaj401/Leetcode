class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        a=sorted(nums)[::-1]
        sum=0
        a=a[:k]
        for i in a:
            if mul>0:
                sum+=i*mul
                mul-=1
            else:
                sum+=i
        return sum