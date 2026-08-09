from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = 0
        total_wait = 0

        for arrival, time in customers:
            current_time = max(current_time, arrival)
            current_time += time

            total_wait += current_time - arrival

        return total_wait / len(customers)