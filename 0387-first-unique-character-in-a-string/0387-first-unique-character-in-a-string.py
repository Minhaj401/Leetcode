class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq=Counter(s)
        for i,ind in enumerate(s):
            if freq[ind]==1:
                return i
        return -1