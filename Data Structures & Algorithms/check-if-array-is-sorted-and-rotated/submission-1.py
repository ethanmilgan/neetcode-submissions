class Solution:
    def check(self, nums):
        decreases = 0
        n = len(nums)

        for i in range(n):
            next_index = (i + 1) % n

            if nums[i] > nums[next_index]:
                decreases += 1

                if decreases > 1:
                    return False

        return True