class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        newnums1 = set(nums1)
        res = []
        for i in nums2:
            if i in newnums1:
                res.append(i)
                newnums1.remove(i)
        return res

result = Solution()
nums1 = [1,2,2,1]
nums2 = [2, 2]
print(result.intersection(nums1, nums2))
