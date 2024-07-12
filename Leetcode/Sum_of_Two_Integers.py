class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            sum_without_carry = a ^ b
            carry = (a & b) << 1
            a, b = sum_without_carry, carry
        return a

res = Solution()
a = 1
b = 2
print(solution.getSum(a, b))
# time limit exceeded