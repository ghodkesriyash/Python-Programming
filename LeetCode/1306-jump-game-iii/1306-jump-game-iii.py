class Solution:
    def canReach(self, arr: List[int], start: int,visited = None) -> bool:
        if visited is None:
            visited = set()
        
        # Already been here, skip
        if start in visited:
            return False
        
        visited.add(start)
        
        if arr[start] == 0:
            return True
        
        next_right = start + arr[start]
        next_left = start - arr[start]
        
        right_valid = 0 <= next_right < len(arr)
        left_valid = 0 <= next_left < len(arr)
        
        if right_valid and self.canReach(arr, next_right, visited):
            return True
        if left_valid and self.canReach(arr, next_left, visited):
            return True
        
        return False       