class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count=0
        for i in arr:
            if i%2!=0:
                count+=1
            elif i%2==0:
                count=0
            
            if count==3:
                return True
            
        return False
        