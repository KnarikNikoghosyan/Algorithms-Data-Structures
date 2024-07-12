class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [i ** 2 for i in nums]
        squares.sort()
        return squares

res = Solution()
nums = [-4, -1, 0, 3, 10]
print(res.sortedSquares(nums))