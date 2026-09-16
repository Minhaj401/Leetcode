class Solution(object):
    def checkPerfectNumber(self, num):
        if num < 2: return False
        s = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                s += i
                if i * i != num:
                    s += num // i
            i += 1
        return s == num