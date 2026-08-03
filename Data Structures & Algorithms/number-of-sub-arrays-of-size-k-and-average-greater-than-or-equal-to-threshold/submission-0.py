from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target_sum = threshold * k
        window_sum = sum(arr[:k])
        count = 0

        if window_sum >= target_sum:
            count += 1

        for right in range(k, len(arr)):
            window_sum += arr[right]
            window_sum -= arr[right - k]

            if window_sum >= target_sum:
                count += 1

        return count