from typing import List
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)
        result = -1

        for num, freq in counts.items():
            if num == freq:
                result = max(result, num)

        return result