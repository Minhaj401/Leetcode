class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []

        for i in nums1:
            index = nums2.index(i)
            found = -1

            for j in range(index + 1, len(nums2)):
                if nums2[j] > i:
                    found = nums2[j]
                    break

            ans.append(found)

        return ans