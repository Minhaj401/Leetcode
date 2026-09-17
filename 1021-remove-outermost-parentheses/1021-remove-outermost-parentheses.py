class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        s = list(s)
        ans = []
        n = len(s)
        opened = 0

        for i in range(n):

            if s[i] == "(":

                if opened > 0:
                    ans.append(s[i])

                opened += 1

            else:

                opened -= 1

                if opened > 0:
                    ans.append(s[i])

        return "".join(ans)