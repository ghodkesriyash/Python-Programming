"""
Question: Container With Most Water
Given an array of heights, find two lines that together with the x-axis
forms a container that holds the most water.
Return the maximum amount of water the container can store.

Categories: Array | Two Pointers | Greedy
"""

def maxArea(self, height: List[int]) -> int:
    """
    Approach: Two Pointer
    Start from both ends and move the pointer with the smaller height inward.
    This is because the area is limited by the shorter line, so moving the
    taller one inward can only decrease the width without any gain.
    """

    left = 0
    right = len(height) - 1
    maxArea = 0

    while left < right:

        """ Calculate area with current left and right pointers
            Area = min height (limiting side) * width (distance between pointers) """
        currentArea = min(height[left], height[right]) * (right - left)

        """ Update maxArea if current area is larger """
        maxArea = max(maxArea, currentArea)

        """ Move the pointer with the smaller height inward
            since keeping the smaller height can never give a larger area """
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxArea