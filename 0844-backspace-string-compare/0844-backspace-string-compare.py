class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a=[]
        b=[]
        for i in s:
            if i !='#':
                a.append(i)
            elif a==[]:
                continue
            else:
                a.pop()
        for i in t:
            if i !='#':
                b.append(i)
            elif b==[]:
                continue
            else:
                b.pop()
        return a==b

