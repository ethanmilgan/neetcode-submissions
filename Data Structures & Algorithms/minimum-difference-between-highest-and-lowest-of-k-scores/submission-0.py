from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        minimum_difference = float("inf")

        for left in range(len(nums) - k + 1):
            right = left + k - 1
            difference = nums[right] - nums[left]
            minimum_difference = min(minimum_difference, difference)

        return minimum_difference