class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cap = capacity
        steps = 0

        for i in range(len(plants)):
            if plants[i] > cap:
                steps += 2 * i
                cap = capacity

            cap -= plants[i]
            steps += 1

        return steps