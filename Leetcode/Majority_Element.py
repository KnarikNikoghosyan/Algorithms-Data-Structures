class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

            if counts[i] > len(nums) // 2:
                return i

res = Solution()
nums = [3, 2, 3]
print(res.majorityElement(nums))
