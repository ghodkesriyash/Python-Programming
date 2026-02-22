# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : NumPy - Filtering with Criteria
# File    : numpy_filtering.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - Filter Roll Numbers by Performance Criteria
#
#   get_roll_nos(data: list, criteria=None) -> list
#
#   Args:
#       data (list): List of (roll_number, marks) tuples.
#       criteria (str, optional): One of the following filters:
#           "above_average" → marks >= mean of all marks
#           "below_average" → marks <= mean of all marks
#           "fail"          → marks <= 40
#           "toppers"       → marks >= 90
#           None            → return all roll numbers
#           invalid string  → return None
#
#   Returns:
#       list of roll numbers matching the criteria, or None if invalid.
# -----------------------------------------------------------------------------

import numpy


def get_roll_nos(data: list, criteria=None):
    """Filter and return roll numbers based on performance criteria."""
    marks = [j[1] for j in data]
    avg   = numpy.mean(marks)

    above_average = [i[0] for i in data if i[1] >= avg]
    below_average = [i[0] for i in data if i[1] <= avg]
    fail          = [i[0] for i in data if i[1] <= 40]
    toppers       = [i[0] for i in data if i[1] >= 90]
    roll          = [i[0] for i in data]

    if criteria is None:
        return roll
    elif criteria == "above_average":
        return above_average
    elif criteria == "below_average":
        return below_average
    elif criteria == "fail":
        return fail
    elif criteria == "toppers":
        return toppers
    else:
        return None                  # invalid criteria


# --- driver code ---
if __name__ == "__main__":
    n    = int(input("enter number of students: "))
    data = []
    for _ in range(n):
        roll, marks = input("enter roll number and marks (space-separated): ").split()
        data.append((int(roll), float(marks)))

    print("all roll nos     :", get_roll_nos(data))
    print("above average    :", get_roll_nos(data, "above_average"))
    print("below average    :", get_roll_nos(data, "below_average"))
    print("fail             :", get_roll_nos(data, "fail"))
    print("toppers          :", get_roll_nos(data, "toppers"))