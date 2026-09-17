class Solution:
    def clearDigits(self, s: str) -> str:

        stack = list()

        for ch in s:
            if ch.islower(): stack.append(ch)
            else: stack.pop()

        return ''.join(stack)