class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        freq = {}
        first_occurrence = {}
        last_occurrence = {}

        for i, num in enumerate(nums):
            if num not in freq:
                freq[num] = 0
                first_occurrence[num] = i
            freq[num] += 1
            last_occurrence[num] = i

        max_degree = max(freq.values())
        min_length = len(nums)

        for num, count in freq.items():
            if count == max_degree:
                min_length = min(min_length, last_occurrence[num] - first_occurrence[num] + 1)

        return min_length

solution = Solution()
nums = [1, 2, 2, 3, 1]
print(solution.findShortestSubArray(nums))