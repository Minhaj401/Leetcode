class Solution(object):
    def simplifyPath(self, path):
        s = path.split('/')
        a = []

        for i in s:
            if i not in ["", ".", ".."]:
                a.append(i)

            elif i == "..":
                if a:
                    a.pop()

        return "/" + "/".join(a)