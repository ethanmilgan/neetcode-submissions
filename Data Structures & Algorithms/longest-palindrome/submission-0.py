class Solution:
    def longestPalindrome(self, s):
        counts = {}
        length = 0

        for char in s:
            counts[char] = counts.get(char, 0) + 1

        has_odd = False

        for frequency in counts.values():
            length += (frequency // 2) * 2

            if frequency % 2 == 1:
                has_odd = True

        if has_odd:
            length += 1

        return length