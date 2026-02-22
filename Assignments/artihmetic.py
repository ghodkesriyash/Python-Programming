# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : Arithmetic Operators & Expressions
# File    : arithmetic_operators.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - Arithmetic Operations
#
# Given two integers a and b from input:
#   output1 : sum of a and b
#   output2 : twice the sum of a and b
#   output3 : absolute difference between a and b
#   output4 : absolute difference between sum and product of a and b
#
# Given price = 80 (int) and discount_percent = 5.75 (float):
#   discounted_price        : price after applying discount (float)
#   rounded_discounted_price: floor of discounted_price (int)
#
# Given total_mins = 470 (int):
#   hrs  : total complete hours using floor division
#   mins : remaining minutes after extracting hours
# -----------------------------------------------------------------------------

a = int(input("enter first number: \n"))
b = int(input("enter second number: \n"))

price, discount_percent = 80, 5.75
total_mins = 470

# --- arithmetic operations ---
output1 = a + b                      # sum
output2 = (a + b) * 2               # twice the sum
output3 = abs(a - b)                 # absolute difference
output4 = abs((a + b) - (a * b))    # abs difference between sum and product

# --- discounted price ---
discounted_price         = price - (price * (discount_percent / 100))  # float
rounded_discounted_price = discounted_price // 1                        # floor value

# --- convert total minutes to hrs and mins ---
hrs  = total_mins // 60              # floor division gives complete hours
mins = total_mins % 60               # modulo gives remaining minutes

print("the sum is %d"                                          % output1)
print("twice the sum is %d"                                    % output2)
print("absolute difference %d"                                 % output3)
print("absolute difference between sum and product of a and b %d" % output4)
print("the discounted price is %d"                             % discounted_price)
print("the rounded discounted price is %d"                     % rounded_discounted_price)
print("the total hours are %d and mins are %d"                 % (hrs, mins))