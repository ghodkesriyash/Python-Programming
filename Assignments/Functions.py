# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : Functions
# File    : functions.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - Multi-Purpose Application Functions
#
# Build a menu-driven program with the following functions:
#
#   odd_num_check(number: int) -> str
#       Returns "yes" if number is odd, else "no"
#
#   perfect_square_check(number: int) -> str
#       Returns "yes" if number is a perfect square, else "no"
#
#   vowel_check(text: str) -> str
#       Returns "yes" if text contains at least one vowel, else "no"
#
#   divisibility_check(number: int) -> str
#       Returns whether number is divisible by 2, 3, both, or neither
#
#   palindrominator(text: str) -> str
#       Builds a palindrome from text by appending its reverse (excluding
#       the last character) e.g. "abc" → "abcba"
#
#   simple_interest(principal_amount: int, n_years: int) -> int
#       Rate is 5% if n_years < 10, else 8%
#       Returns rounded simple interest
#
# main() reads the operation name from input, then reads required arguments
# and calls the corresponding function.
# -----------------------------------------------------------------------------

import math


def odd_num_check(number: int) -> str:
    """Returns 'yes' if number is odd, else 'no'."""
    return "yes" if number % 2 != 0 else "no"


def perfect_square_check(number: int) -> str:
    """Returns 'yes' if number is a perfect square, else 'no'."""
    root = int(math.sqrt(number))
    return "yes" if root * root == number else "no"


def vowel_check(text: str) -> str:
    """Returns 'yes' if text contains at least one vowel, else 'no'."""
    vowels = "aeiouAEIOU"
    return "yes" if any(char in vowels for char in text) else "no"


def divisibility_check(number: int) -> str:
    """Returns divisibility status of number with respect to 2 and 3."""
    if number % 2 == 0 and number % 3 == 0:
        return "divisible by 2 and 3"
    elif number % 2 == 0:
        return "divisible by 2"
    elif number % 3 == 0:
        return "divisible by 3"
    else:
        return "not divisible by 2 and 3"


def palindrominator(text: str) -> str:
    """Builds a palindrome from text e.g. 'abc' → 'abcba'."""
    return text + text[-2::-1] if len(text) > 0 else text


def simple_interest(principal_amount: int, n_years: int) -> int:
    """Returns rounded simple interest. Rate: 5% if n_years < 10, else 8%."""
    rate     = 0.05 if n_years < 10 else 0.08
    interest = principal_amount * rate * n_years
    return round(interest)


def main():
    operation = input().strip()

    if operation == "odd_num_check":
        print(odd_num_check(int(input())))

    elif operation == "perfect_square_check":
        print(perfect_square_check(int(input())))

    elif operation == "vowel_check":
        print(vowel_check(input().strip()))

    elif operation == "divisibility_check":
        print(divisibility_check(int(input())))

    elif operation == "palindrominator":
        print(palindrominator(input().strip()))

    elif operation == "simple_interest":
        principal_amount = int(input())
        n_years          = int(input())
        print(simple_interest(principal_amount, n_years))


main()