
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        s = []

        for i in asteroids:
            while s and s[-1] > 0 and i < 0 and s[-1] + i < 0:
                s.pop()

            if s and s[-1] > 0 and i < 0:
                if s[-1] + i == 0:
                    s.pop()
                continue

            s.append(i)

        return s
