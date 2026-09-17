class Solution:
    def makeGood(self, s: str) -> str:

        def makegreat(s):
            n = len(s)

            for i in range(n - 1):
                if ((s[i].islower() and s[i+1].isupper()) or
                    (s[i].isupper() and s[i+1].islower())) and s[i].lower() == s[i+1].lower():

                    s = s[:i] + s[i+2:]
                    return makegreat(s)

            return s

        return makegreat(s)