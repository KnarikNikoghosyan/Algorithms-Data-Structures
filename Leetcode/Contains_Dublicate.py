class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        ls = set()
        for i in nums:
            if i in ls:
                return True
            ls.add(i)
        return False

nums = [2, 4, 9, 2, 8]
print(Solution().containsDuplicate(nums))