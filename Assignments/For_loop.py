# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : For Loops (no while loops allowed, max 7 for loops)
# File    : for_loops.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - For Loop Tasks (while loops are NOT allowed, max 7 for loops)
#
#   factorial
#       Read n. Print the factorial of n using accumulation.
#
#   even_numbers
#       Read n. Print all even numbers from 0 to n (inclusive).
#
#   power_sequence
#       Read n. Print the first n powers of 2 starting from 2^0 (1, 2, 4...).
#
#   sum_not_divisible
#       Read n. Print sum of all numbers from 1 to n-1
#       that are NOT divisible by 4 or 5.
#
#   from_k
#       Read n and k. Starting from k downwards, find n odd numbers
#       that don't contain digit 5 or 9. Print each number reversed.
#
#   string_iter
#       Read a string of digits. For each digit, print it multiplied
#       by the previous digit (starting with prev = 1).
#
#   list_iter
#       Read a Python list (e.g. [1, 2.0, 'three', True]).
#       For each item print: "<item> - type: <type>"
# -----------------------------------------------------------------------------

# Note: the self-referencing prefix checker is omitted (not needed standalone).

task = input()

if task == "factorial":                 # accumulation
    n      = int(input())
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(result)

elif task == "even_numbers":            # plain iteration
    n = int(input())
    for i in range(0, n + 1, 2):       # step 2 hits every even; includes 0 and n if even
        print(i)

elif task == "power_sequence":          # mapping
    n      = int(input())
    result = 1
    for i in range(n):
        print(result)
        result *= 2

elif task == "sum_not_divisible":       # filtered accumulation
    n     = int(input())
    total = 0
    for i in range(1, n):              # 1 to n-1
        if i % 4 != 0 and i % 5 != 0:
            total += i
    print(total)

elif task == "from_k":                  # filtering + mapping
    n     = int(input())
    k     = int(input())
    count = 0
    for i in range(k, 0, -1):          # count down from k to 1
        if count == n:
            break
        if i % 2 == 1 and "5" not in str(i) and "9" not in str(i):
            print(str(i)[::-1])        # print the number reversed
            count += 1

elif task == "string_iter":             # iterable mapping over string digits
    s    = input().strip()
    prev = 1
    for ch in s:
        curr = int(ch)
        print(curr * prev)
        prev = curr

elif task == "list_iter":               # iterable mapping over a list
    l = eval(input())                   # reads list like [1, 2.0, 'three', True]
    for item in l:
        print(f"{item} - type: {type(item)}")

else:
    print("Invalid")