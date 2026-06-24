class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = sorted(point[0] for point in points)

        ans = 0
        for i in range(1, len(xs)):
            ans = max(ans, xs[i] - xs[i - 1])

        return ans