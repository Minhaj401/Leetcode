class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return f"{n:b}"[0] == "1" and "1" not in f"{n:b}"[1:]