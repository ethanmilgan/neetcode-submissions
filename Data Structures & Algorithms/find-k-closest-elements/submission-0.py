from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) // 2

            left_distance = x - arr[mid]
            right_distance = arr[mid + k] - x

            if left_distance > right_distance:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]