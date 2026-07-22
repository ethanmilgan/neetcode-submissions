class Solution:
    def findErrorNums(self, nums):
        counts = {}
        duplicate = -1
        missing = -1

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for i in range(1, len(nums) + 1):
            if counts.get(i, 0) == 2:
                duplicate = i
            elif counts.get(i, 0) == 0:
                missing = i

        return [duplicate, missing]