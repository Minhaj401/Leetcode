class Solution(object):
    def findArray(self, pref: List[int]) -> List[int]:
        l = len(pref)
        a = [0] * l
        a[0] = pref[0]
        for i in range(1, l):
            a[i] = pref[i] ^ pref[i - 1]
        return a