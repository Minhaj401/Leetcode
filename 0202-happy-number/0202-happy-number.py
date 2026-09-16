class Solution:
    def isHappy(self, n: int) -> bool:
        num = 0
        sum = 0

        while num < 50 and sum != 1:
            sum = 0

            for i in str(n):
                sum += int(i) * int(i)

            n = sum
            num += 1

        return sum == 1