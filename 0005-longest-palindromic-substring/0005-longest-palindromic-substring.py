class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""

        r = 0
        while r < n:
            l = r

            while l < n:
                sub = s[r:l+1]

                if sub == sub[::-1]:
                    if len(sub) > len(ans):
                        ans = sub

                l += 1

            r += 1

        return ans