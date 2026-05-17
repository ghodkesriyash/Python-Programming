"""
Question: Given an array of non-negative integers arr and a start index, return
true if you can reach any index with value 0. From index i you can jump to
i + arr[i] or i - arr[i], and you may not visit the same index twice.

Logic: Recursive DFS from start index, tracking visited indices to avoid cycles.
At each index attempt both left and right jumps if within bounds, return True
if any path reaches a zero-valued index.
"""

class Solution:
    def canReach(self, arr: list[int], start: int, visited=None) -> bool:
        if visited is None:
            visited = set()

        if start in visited:
            return False        # Already visited, avoid cycle

        visited.add(start)

        if arr[start] == 0:
            return True         # Reached a zero-valued index

        next_right = start + arr[start]
        next_left = start - arr[start]

        right_valid = 0 <= next_right < len(arr)  # Bounds check right jump
        left_valid = 0 <= next_left < len(arr)    # Bounds check left jump

        if right_valid and self.canReach(arr, next_right, visited):
            return True
        if left_valid and self.canReach(arr, next_left, visited):
            return True

        return False