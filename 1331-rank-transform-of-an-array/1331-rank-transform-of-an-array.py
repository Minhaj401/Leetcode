class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr)==0:
            return []
        s=sorted(arr)
        a={}
        a[s[0]]=1
        k=1
        m=s[0]
        for i in range(1,len(arr)):
            if s[i] >m:
                k+=1
                m=s[i]
                a[s[i]]=k
        x=[a[i] for i in arr]
        return x
