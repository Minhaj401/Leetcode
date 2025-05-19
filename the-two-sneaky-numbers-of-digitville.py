class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[]
        for i in nums:
            if nums.count(i)>1:
                answer.append(i)
                nums.remove(i)
        return answer