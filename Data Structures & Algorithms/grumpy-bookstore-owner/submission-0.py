class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        always_satisfied = 0
        extra_satisfied = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                always_satisfied += customers[i]

        for i in range(minutes):
            if grumpy[i] == 1:
                extra_satisfied += customers[i]

        max_extra = extra_satisfied

        for right in range(minutes, len(customers)):
            if grumpy[right] == 1:
                extra_satisfied += customers[right]

            left = right - minutes

            if grumpy[left] == 1:
                extra_satisfied -= customers[left]

            max_extra = max(max_extra, extra_satisfied)

        return always_satisfied + max_extra