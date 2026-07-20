class Solution:
    def divideArray(self, nums):
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for frequency in counts.values():
            if frequency % 2 != 0:
                return False

        return True