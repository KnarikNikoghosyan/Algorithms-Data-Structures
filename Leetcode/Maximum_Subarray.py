class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_current = maxx = nums[0]

        for i in nums[1:]:
            max_current = max(i, max_current + i)
            if max_current > maxx:
                maxx = max_current

        return maxx

res = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(res.maxSubArray(nums))
