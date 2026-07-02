class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a={}
        for i in nums:
            if i not in a:
                a[i]=0
            a[i]+=1
        k=[]
        while a!={}:

            m=[]
            for i in list(a.keys()):
                if a[i]!=0:
                    m.append(i)
                    a[i]-=1
                if a[i]==0:
                    del a[i]
            k.append(m)
        return k
                