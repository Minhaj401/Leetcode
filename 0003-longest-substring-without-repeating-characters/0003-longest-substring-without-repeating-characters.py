class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi=0
        low=0
        high=0
        while high<len(s):
            if len(s[low:high+1])==len(set(s[low:high+1])):
                maxi=max(maxi,high-low+1)
                high+=1
            else:
                low+=1
        return maxi