class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        return int(n * (n+1) / 2 - sum(nums))

#Sum of 0..n minus sum of the given numbers is the missing one.

