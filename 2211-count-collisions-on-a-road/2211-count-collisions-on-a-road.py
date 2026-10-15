class Solution:
    def countCollisions(self, directions: str) -> int:
        return len(directions.lstrip('L').rstrip('R').replace('S',''))