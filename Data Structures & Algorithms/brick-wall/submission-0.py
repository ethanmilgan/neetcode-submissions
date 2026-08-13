from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_count = {}

        for row in wall:
            position = 0

            # Skip the final brick so we don't count the right wall edge
            for brick in row[:-1]:
                position += brick
                edge_count[position] = edge_count.get(position, 0) + 1

        max_edges = 0

        for count in edge_count.values():
            max_edges = max(max_edges, count)

        return len(wall) - max_edges