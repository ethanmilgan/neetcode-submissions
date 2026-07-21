class Solution:
    def minOperations(self, s):
        start_with_zero = 0
        start_with_one = 0

        for i in range(len(s)):
            expected_zero = "0" if i % 2 == 0 else "1"
            expected_one = "1" if i % 2 == 0 else "0"

            if s[i] != expected_zero:
                start_with_zero += 1

            if s[i] != expected_one:
                start_with_one += 1

        return min(start_with_zero, start_with_one)