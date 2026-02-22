# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : String Slicing & Indexing
# File    : string_slicing.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - String Slicing & Indexing
#
# Given a string `s` and a `course_code` in format "YYtTcsXXXX"
# where YY = year, T = term number, csXXXX = course id:
#
#   output1 : get the third character of s
#   output2 : get the fourth last character of s
#   output3 : get the first 3 characters of s
#   output4 : get every second character of s
#   output5 : get the last 3 characters of s
#   output6 : get the reverse of s
#
#   course_term (int) : extract the term number from course_code
#   course_year (int) : extract the 2-digit year from course_code
# -----------------------------------------------------------------------------

s           = "hello pyhton"
course_code = "24t2cs1002"   # format: YY t T csXXXX

output1 = s[2]       # third character
output2 = s[-4]      # fourth last character
output3 = s[:3]      # first 3 characters
output4 = s[::2]     # every second character
output5 = s[-3:]     # last 3 characters
output6 = s[::-1]    # reverse of s

course_term = int(course_code[3])     # term number as int
course_year = int(course_code[0:2])   # 2-digit year as int

print(course_code, "this is the course code, ", s, "is the string")
print("third character is %s"      % output1)
print("fourth last character is %s" % output2)
print("first three characters are %s" % output3)
print("every second character is %s"  % output4)
print("last 3 characters are %s"      % output5)
print("reverse string is %s"          % output6)
print("course term is %s"             % course_term)
print("course year is %s"             % course_year)

