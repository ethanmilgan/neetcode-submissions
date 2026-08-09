from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        vowels = {"a", "e", "i", "o", "u"}
        prefix = [0] * (len(words) + 1)

        for i in range(len(words)):
            prefix[i + 1] = prefix[i]

            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i + 1] += 1

        result = []

        for left, right in queries:
            count = prefix[right + 1] - prefix[left]
            result.append(count)

        return result