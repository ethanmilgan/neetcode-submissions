class Solution:
    def countCharacters(self, words, chars):
        available = {}

        for char in chars:
            available[char] = available.get(char, 0) + 1

        total_length = 0

        for word in words:
            needed = {}

            for char in word:
                needed[char] = needed.get(char, 0) + 1

            can_form = True

            for char, count in needed.items():
                if count > available.get(char, 0):
                    can_form = False
                    break

            if can_form:
                total_length += len(word)

        return total_length