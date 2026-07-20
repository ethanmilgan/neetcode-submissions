class Solution:
    def numIdenticalPairs(self, nums):
        counts = {}
        good_pairs = 0

        for num in nums:
            good_pairs += counts.get(num, 0)
            counts[num] = counts.get(num, 0) + 1

        return good_pairs