class Solution:
    def clearDigits(self, s: str) -> str:

        stack = deque()

        for ch in s:
            if ch.islower(): stack.append(ch)
            else: stack.pop()

        return ''.join(stack)