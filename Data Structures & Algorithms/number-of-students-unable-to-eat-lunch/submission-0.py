from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        preferences = [0, 0]

        for student in students:
            preferences[student] += 1

        for sandwich in sandwiches:
            if preferences[sandwich] == 0:
                return preferences[0] + preferences[1]

            preferences[sandwich] -= 1

        return 0