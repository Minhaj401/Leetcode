class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sublists = [arr[i:j] for i in range(len(arr) + 1) for j in range(i + 1, len(arr) + 1)]
        ss=0
        for i in sublists:
            if len(i)%2!=0:
                a=sum(i)
                ss+=a
        return ss
