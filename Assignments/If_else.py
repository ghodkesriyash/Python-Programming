# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : If-Else Patterns
# File    : if_else_patterns.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - Part 1 : Basic If
#
# Given a word (str) and a boolean `continuous_tense`:
#   - If the word already ends with "ing" and `continuous_tense` is False,
#     remove the "ing" suffix.
#   - If the word does NOT end with "ing" and `continuous_tense` is True,
#     add the "ing" suffix.
# -----------------------------------------------------------------------------

word = "glow"          # str
continuous_tense = True  # bool

new_word = word  # do not remove this line

if new_word.endswith("ing"):
    if not continuous_tense:
        new_word = new_word[:-3]          # remove "ing" suffix
elif continuous_tense:
    new_word = new_word + "ing"           # add "ing" suffix

print(f"new_word: {new_word}")


# -----------------------------------------------------------------------------
# QUESTION - Part 2 : If-Else Pattern
#
# Given `age` (int) and `is_member` (bool):
#   - Determine `age_group`: "Adult" if age >= 18, else "Child"
#   - Determine `applicant_type` by combining age group and membership status.
#     e.g. "Adult Member", "Child Non-member"
# -----------------------------------------------------------------------------

age = 5           # int
is_member = True  # bool

age_group = "Adult" if age >= 18 else "Child"

member_status = "Member" if is_member else "Non-member"
applicant_type = f"{age_group} {member_status}"

print(f"age_group     : {age_group}")
print(f"applicant_type: {applicant_type}")


# -----------------------------------------------------------------------------
# QUESTION - Part 3 : If ... Elif ... Else
#
# Given `color_code` (str): valid values are R, G, B
#   - Assign `color` in lowercase ("red", "green", "blue")
#   - Assign "black" if the code is unrecognized
#
# Given `time` (str) in format "HH AM/PM" (hour ranges 1–12):
#   - `is_time_valid` (bool): True if hour is between 1 and 12 (inclusive)
#   - `time_in_hrs` (int)  : time converted to 24-hour format
#   - `time_of_day` (str)  : one of Morning / Afternoon / Evening / Night
#       Morning   → 6 AM  to 12 PM  (includes 6 AM,  excludes 12 PM)
#       Afternoon → 12 PM to 6 PM   (includes 12 PM, excludes 6 PM)
#       Evening   → 6 PM  to 12 AM  (includes 6 PM,  excludes 12 AM)
#       Night     → 12 AM to 6 AM   (includes 12 AM, excludes 6 AM)
#     Use "Invalid" if the hour is outside the acceptable range.
# -----------------------------------------------------------------------------

color_code = "R"      # str: R, G, or B
time = "02 PM"        # str: format "[2-digit hour] [AM or PM]"

# --- color ---
color_map = {"R": "red", "G": "green", "B": "blue"}
color = color_map.get(color_code, "black")

# --- time ---
parts = time.split()
time_inhrs = int(parts[0])
period = parts[1]

is_time_valid = 1 <= time_inhrs <= 12

# Convert to 24-hour: 12 AM → 0, 12 PM → 12, x AM → x, x PM → x + 12
time_in_hrs = (time_inhrs % 12) + (12 if period == "PM" else 0)

if not is_time_valid:
    time_of_day = "Invalid"
elif 6 <= time_in_hrs < 12:
    time_of_day = "Morning"
elif 12 <= time_in_hrs < 18:
    time_of_day = "Afternoon"
elif 18 <= time_in_hrs < 24:
    time_of_day = "Evening"
else:                                     # 0 <= time_in_hrs < 6
    time_of_day = "Night"

print(f"color        : {color}")
print(f"is_time_valid: {is_time_valid}")
print(f"time_in_hrs  : {time_in_hrs}")
print(f"time_of_day  : {time_of_day}")