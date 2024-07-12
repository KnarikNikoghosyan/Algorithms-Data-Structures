class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}

        for i, j in enumerate(nums):
            if((target - j) in di):
                return di[target - j], i
            else:
                di.update({j: i})
        return -1