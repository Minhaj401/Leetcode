class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        a = []
        nums.sort()

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr = nums[i] + nums[left] + nums[right]

                if curr == 0:
                    a.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left +=1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif curr > 0:
                    right -= 1
                else:
                    left += 1

        return a