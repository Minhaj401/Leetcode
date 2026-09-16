class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=[i for i in s]
        a=0
        b=len(s)-1
        while a<b:
            if s[a] not in "AaEeIiOoUu":
                a+=1
            if s[b] not in "AaEeIiOoUu":
                b-=1
            if s[a] in "AaEeIiOoUu" and s[b]in "AaEeIiOoUu":
                temp=s[a]
                s[a]=s[b]
                s[b]=temp

                a+=1
                b-=1
        return "".join(s)
