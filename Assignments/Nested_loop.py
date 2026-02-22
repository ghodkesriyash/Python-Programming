# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : Nested For Loops
# File    : nested_for_loops.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - Nested For Loop Tasks
#
#   permutation
#       Read a string s. Print all 2-character permutations of its characters
#       (no character paired with itself), in order.
#
#   sorted_permutation
#       Read a string s. Print all 2-character permutations where the first
#       character comes alphabetically before the second.
#
#   repeat_the_repeat
#       Read n. Build a string "123...n" and print it n times.
#
#   repeat_incrementally
#       Read n. Print n lines where line i contains "123...i".
#       e.g. n=3 → "1", "12", "123"
#
#   increment_and_decrement
#       Read n. Print n lines where line i contains "123...i...21"
#       (counts up to i then back down, excluding i in the descent).
#       e.g. i=3 → "12321"
# -----------------------------------------------------------------------------

task = input()

if task == "permutation":               # nested loop over all pairs (i, j), i ≠ j
    s = input().strip()
    n = len(s)
    for i in range(n):
        for j in range(n):
            if i != j:
                print(s[i] + s[j])

elif task == "sorted_permutation":      # same as above but only alphabetical order pairs
    s = input().strip()
    n = len(s)
    for i in range(n):
        for j in range(n):
            if i != j and s[i] < s[j]:
                print(s[i] + s[j])

elif task == "repeat_the_repeat":       # build once, print n times
    n    = int(input())
    line = "".join(str(i) for i in range(1, n + 1))
    for _ in range(n):
        print(line)

elif task == "repeat_incrementally":    # each line grows by one digit
    n = int(input())
    for i in range(1, n + 1):
        print("".join(str(j) for j in range(1, i + 1)))

elif task == "increment_and_decrement": # count up to i then back down (no repeat of i)
    n = int(input())
    for i in range(1, n + 1):
        inc = "".join(str(j) for j in range(1, i + 1))
        dec = "".join(str(j) for j in range(i - 1, 0, -1))
        print(inc + dec)

else:
    print("Invalid")