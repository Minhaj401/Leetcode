class Solution(object):
    def addStrings(self, num1, num2):
        n = len(num1)
        m = len(num2)

        if n > m: num2 = '0' * (n-m) + num2
        elif m > n: num1 = '0' * (m-n) + num1

        num1r = num1[::-1]
        num2r = num2[::-1]

        ans = ""
        carry = 0
        for n1,n2 in zip(num1r,num2r):
            x = (ord(n1) - 48) + (ord(n2)-48) + carry

            if x > 9:
                ans = str(x%10) + ans 
                carry = x//10
            else:
                ans = str(x) + ans
                carry = 0

        if carry != 0:
            ans = str(carry) + ans

        return ans