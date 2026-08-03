from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        window_sum = 0
        max_frequency = 1

        for right in range(len(nums)):
            window_sum += nums[right]

            while (
                nums[right] * (right - left + 1) - window_sum > k
            ):
                window_sum -= nums[left]
                left += 1

            max_frequency = max(
                max_frequency,
                right - left + 1
            )

        return max_frequency