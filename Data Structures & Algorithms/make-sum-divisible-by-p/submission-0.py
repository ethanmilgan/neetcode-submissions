from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p

        if target == 0:
            return 0

        last_seen = {0: -1}
        prefix = 0
        answer = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p

            needed = (prefix - target) % p

            if needed in last_seen:
                answer = min(answer, i - last_seen[needed])

            last_seen[prefix] = i

        return answer if answer < len(nums) else -1