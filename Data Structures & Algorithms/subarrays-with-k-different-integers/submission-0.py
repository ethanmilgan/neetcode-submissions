from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most(limit: int) -> int:
            counts = {}
            left = 0
            total = 0

            for right, num in enumerate(nums):
                counts[num] = counts.get(num, 0) + 1

                while len(counts) > limit:
                    left_num = nums[left]
                    counts[left_num] -= 1

                    if counts[left_num] == 0:
                        del counts[left_num]

                    left += 1

                total += right - left + 1

            return total

        return at_most(k) - at_most(k - 1)