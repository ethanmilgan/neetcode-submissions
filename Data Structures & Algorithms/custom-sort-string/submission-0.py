class Solution:
    def customSortString(self, order: str, s: str) -> str:
        frequency = {}

        for char in s:
            frequency[char] = frequency.get(char, 0) + 1

        result = []

        for char in order:
            if char in frequency:
                result.append(char * frequency[char])
                del frequency[char]

        for char, count in frequency.items():
            result.append(char * count)

        return "".join(result)