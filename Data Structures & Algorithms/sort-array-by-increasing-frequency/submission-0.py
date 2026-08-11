from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        nums.sort(key=lambda num: (frequency[num], -num))

        return nums