class Solution:
    def maxLengthBetweenEqualCharacters(self, s):
        first_position = {}
        longest = -1

        for i, char in enumerate(s):
            if char in first_position:
                distance = i - first_position[char] - 1
                longest = max(longest, distance)
            else:
                first_position[char] = i

        return longest