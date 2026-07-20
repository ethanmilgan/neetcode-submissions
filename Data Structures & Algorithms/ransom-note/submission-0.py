class Solution:
    def canConstruct(self, ransomNote, magazine):
        counts = {}

        # Count the letters in magazine
        for char in magazine:
            counts[char] = counts.get(char, 0) + 1

        # Use the letters to build the ransom note
        for char in ransomNote:
            if counts.get(char, 0) == 0:
                return False

            counts[char] -= 1

        return True