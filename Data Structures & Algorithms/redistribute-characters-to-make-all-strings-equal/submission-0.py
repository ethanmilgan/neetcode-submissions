class Solution:
    def makeEqual(self, words):
        counts = {}
        number_of_words = len(words)

        for word in words:
            for char in word:
                counts[char] = counts.get(char, 0) + 1

        for frequency in counts.values():
            if frequency % number_of_words != 0:
                return False

        return True