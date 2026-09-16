class Solution(object):
    def selfDividingNumbers(self, left, right):
        z = []

        for i in range(left, right + 1):
            a = 1

            for k in str(i):
                if k == '0':
                    a = 0
                    break

                if i % int(k) != 0:
                    a = 0
                    break

            if a == 1:
                z.append(i)

        return z