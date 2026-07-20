class Solution:
    def countConsistentStrings(self, allowed, words):
        allowed_chars = set(allowed)
        consistent_count = 0

        for word in words:
            is_consistent = True

            for char in word:
                if char not in allowed_chars:
                    is_consistent = False
                    break

            if is_consistent:
                consistent_count += 1

        return consistent_count