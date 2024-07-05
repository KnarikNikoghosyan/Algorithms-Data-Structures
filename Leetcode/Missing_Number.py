class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        num_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i

res = Solution()
nums = [3, 0, 1]
print(res.missingNumber(nums))
