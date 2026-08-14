from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Step 1: Find the dominant element
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        # Step 2: Count its total occurrences
        total = 0

        for num in nums:
            if num == candidate:
                total += 1

        # Step 3: Find the earliest valid split
        left_count = 0
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == candidate:
                left_count += 1

            left_length = i + 1
            right_length = n - i - 1
            right_count = total - left_count

            if (
                left_count * 2 > left_length
                and right_count * 2 > right_length
            ):
                return i

        return -1