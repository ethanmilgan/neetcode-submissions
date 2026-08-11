from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        frequency = {}

        for num in arr1:
            frequency[num] = frequency.get(num, 0) + 1

        result = []

        # Add elements in arr2 order
        for num in arr2:
            result.extend([num] * frequency[num])
            del frequency[num]

        # Add remaining elements in ascending order
        remaining = []

        for num, count in frequency.items():
            remaining.extend([num] * count)

        remaining.sort()
        result.extend(remaining)

        return result