from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_counts = {0: 1}
        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num

            result += prefix_counts.get(prefix_sum - goal, 0)

            prefix_counts[prefix_sum] = (
                prefix_counts.get(prefix_sum, 0) + 1
            )

        return result