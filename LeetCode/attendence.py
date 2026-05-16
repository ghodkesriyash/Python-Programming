"""
Question: Given a string s representing an attendance record, return true if the
student is eligible for an attendance award. A student is eligible if they have
strictly fewer than 2 absences ('A') and no 3 or more consecutive lates ('L').

Logic: Count total absences, fail if 2 or more, then check for
three consecutive lates as a substring, return True if both checks pass.
"""

class Solution:
    def checkRecord(self, s: str) -> bool:
        count = 0
        for i in s:
            if i == "A":
                count += 1  # Count total absences
        if count >= 2:
            return False    # Fail if 2 or more absences
        if "LLL" in s:
            return False    # Fail if 3 or more consecutive lates
        return True