class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = {}
        for i in nums:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1

        for count in a.values():
            if count > 1:
                return True

        return False