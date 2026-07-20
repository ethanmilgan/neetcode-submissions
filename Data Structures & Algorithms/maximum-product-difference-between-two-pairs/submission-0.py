class Solution:
    def maxProductDifference(self, nums):
        nums.sort()

        largest_product = nums[-1] * nums[-2]
        smallest_product = nums[0] * nums[1]

        return largest_product - smallest_product