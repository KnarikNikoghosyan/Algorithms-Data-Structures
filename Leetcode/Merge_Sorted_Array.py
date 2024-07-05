class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int):
        ln = len(nums1) -1
        while n:
            if not m:
                for i in range(0, n):
                    nums1[i] = nums2[i]
                return nums1
            if nums1[m - 1] < nums2[n -1]:
                nums1[ln] = nums2[n -1]
                n -= 1
                ln -= 1
            else:
                nums1[m - 1], nums1[ln] = nums1[ln], nums2[m - 1]
                m -= 1
                ln -= 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2, 5, 6]
n = 3
res = Solution()
print(res.merge(nums1, m, nums2, n))
