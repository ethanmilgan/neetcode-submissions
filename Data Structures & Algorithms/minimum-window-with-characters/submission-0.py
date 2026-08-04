from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        required = Counter(t)
        window = defaultdict(int)

        required_types = len(required)
        formed_types = 0

        left = 0
        best_length = float("inf")
        best_start = 0

        for right, char in enumerate(s):
            window[char] += 1

            if char in required and window[char] == required[char]:
                formed_types += 1

            while formed_types == required_types:
                window_length = right - left + 1

                if window_length < best_length:
                    best_length = window_length
                    best_start = left

                left_char = s[left]
                window[left_char] -= 1

                if (
                    left_char in required
                    and window[left_char] < required[left_char]
                ):
                    formed_types -= 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_start:best_start + best_length]