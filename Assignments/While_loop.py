# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : While Loops (no for loops allowed)
# File    : while_loops.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - While Loop Tasks (for loops are NOT allowed)
#
# A prefix check in the original file ensures no `for` loops are used.
# Based on the `task` input, run one of the following:
#
#   sum_until_0
#       Keep reading integers and accumulate their sum until 0 is entered.
#       Print the total.
#
#   total_price
#       Keep reading "quantity price" pairs until "END".
#       Print the total price (sum of quantity * price for each line).
#
#   only_ed_or_ing
#       Keep reading words until "stop" (case-insensitive).
#       Print only words that end with "ed" or "ing" (one per line).
#
#   reverse_sum_palindrome
#       Keep reading integers until -1.
#       For each number n, check if n + reverse(n) is a palindrome.
#       Print all such n values (one per line).
#
#   double_string
#       Keep reading strings until an empty line.
#       Print each string doubled (e.g. "hi" → "hihi").
#
#   odd_char
#       Keep reading strings until one ends with ".".
#       For each string, extract characters at odd positions (1st, 3rd, 5th...).
#       Print all results space-separated.
#
#   only_even_squares
#       Keep reading integers until "NAN".
#       Print the square of each even number (one per line).
#
#   only_odd_lines
#       Keep reading lines until "END".
#       Print only odd-numbered lines (1st, 3rd, 5th...) in reverse order.
# -----------------------------------------------------------------------------

# Note: prefix code block that checks for 'for' loops is omitted here
# since this file is not self-referencing. The logic is identical.

task = input()

if task == "sum_until_0":
    total = 0
    n = int(input())
    while n != 0:
        total += n
        n = int(input())
    print(total)

elif task == "total_price":
    total_price = 0
    while True:
        line = input()
        if line == "END":
            break
        quantity, price = line.split()
        total_price += int(quantity) * int(price)
    print(total_price)

elif task == "only_ed_or_ing":
    words = []
    while True:
        s = input()
        if s.lower() == "stop":
            break
        if s.lower().endswith("ed") or s.lower().endswith("ing"):
            words.append(s)
    print("\n".join(words))

elif task == "reverse_sum_palindrome":
    def is_palindrome(num):
        s = str(num)
        return s == s[::-1]

    nums = []
    while True:
        a = input()
        if a == "-1":
            break
        n   = int(a)
        rev = int(str(n)[::-1])
        if is_palindrome(n + rev):
            nums.append(str(n))
    print("\n".join(nums))

elif task == "double_string":
    lines = []
    while True:
        s = input()
        if s == "":
            break
        lines.append(s * 2)
    print("\n".join(lines))

elif task == "odd_char":
    result = []
    while True:
        s         = input()
        odd_chars = ""
        i         = 0
        while i < len(s):
            if (i + 1) % 2 != 0:   # positions 1, 3, 5... (1-indexed)
                odd_chars += s[i]
            i += 1
        result.append(odd_chars)
        if s.endswith("."):         # process last string then stop
            break
    print(" ".join(result))

elif task == "only_even_squares":
    squares = []
    while True:
        s = input()
        if s == "NAN":
            break
        n = int(s)
        if n % 2 == 0:
            squares.append(str(n ** 2))
    print("\n".join(squares))

elif task == "only_odd_lines":
    lines = []
    count = 1
    while True:
        s = input()
        if s == "END":
            break
        if count % 2 != 0:
            lines.insert(0, s)      # prepend to build reverse order naturally
        count += 1
    print("\n".join(lines))