class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_index = 0
        abbr_index = 0

        while word_index < len(word) and abbr_index < len(abbr):
            if abbr[abbr_index].isalpha():
                if word[word_index] != abbr[abbr_index]:
                    return False

                word_index += 1
                abbr_index += 1

            else:
                if abbr[abbr_index] == "0":
                    return False

                skip = 0

                while abbr_index < len(abbr) and abbr[abbr_index].isdigit():
                    skip = skip * 10 + int(abbr[abbr_index])
                    abbr_index += 1

                word_index += skip

        return word_index == len(word) and abbr_index == len(abbr)