# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : Variables, Swap & Circular Swap
# File    : swap_operations.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - Part 1 : Simple Swap
#
# Take 6 inputs: x1, x2, y1, y2, y3, z
#   - Swap the values of x1 and x2
#
# QUESTION - Part 2 : Circular Swap
#   - Circularly swap y1, y2, y3 such that: y1 = y2, y2 = y3, y3 = y1
#
# QUESTION - Part 3 : Variable Operations
#   - Create a new variable `a` with the value of `z`
#   - Delete the variable `z`
#   - Print x1, x2, y1, y2, y3, a in order
# -----------------------------------------------------------------------------

x1 = input("enter x1 :")
x2 = input("enter x2 :")
y1 = input("enter y1 :")
y2 = input("enter y2 :")
y3 = input("enter y3 :")
z  = input("enter z  :")

# swap x1 and x2
x1, x2 = x2, x1

# circular swap: y1 → y2 → y3 → y1
y1, y2, y3 = y2, y3, y1

# create `a` from `z`, then delete `z`
a = z
del z

print(x1)
print(x2)
print(y1)
print(y2)
print(y3)
print(a)
