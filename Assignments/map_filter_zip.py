# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : map, filter, zip, enumerate & lambda
# File    : map_filter_zip.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - Functional Programming Tools
#
#   is_greater_than_5(numbers: list) -> list
#       Return a list of bools: True where number > 5, using map + lambda.
#
#   filter_less_than_5(numbers: list) -> list
#       Return only numbers less than 5, using filter + lambda.
#
#   sum_of_two_digit_numbers(numbers: list)
#       Return sum of all two-digit numbers (10-99, sign-agnostic),
#       using sum + filter + lambda.
#
#   is_all_has_a(words: list) -> bool
#       Return True if every word contains the letter 'a' (case-insensitive),
#       using all + map + lambda.
#
#   print_with_numbering(items)
#       Print each item on its own line with 1-based numbering.
#       e.g. ["apple","orange"] → "1. apple\n2. orange"
#
#   parallel_print(countries, capitals)
#       Print each country-capital pair separated by " - ".
#       Stops at the shorter list (zip behaviour).
#
#   make_dict(keys, values) -> dict
#       Create a dict by zipping keys and values together.
#
#   indices_of_big_words(words) -> list
#       Return indices of words with length > 5,
#       using enumerate + filter + map + lambda.
#
#   decode_rle(chars: str, repeats: list) -> str
#       Return string where each char is repeated by its paired repeat count.
#       Uses zip + map + join. (RLE = Run-Length Encoding)
#       e.g. "abc", [2,3,1] → "aabbbbc"
# -----------------------------------------------------------------------------


def is_greater_than_5(numbers: list) -> list:
    """Return list of bools: True where number > 5."""
    return list(map(lambda x: x > 5, numbers))


def filter_less_than_5(numbers: list) -> list:
    """Return only numbers strictly less than 5."""
    return list(filter(lambda x: x < 5, numbers))


def sum_of_two_digit_numbers(numbers: list):
    """Return sum of all two-digit numbers (10 ≤ |x| ≤ 99)."""
    return sum(filter(lambda x: 10 <= abs(x) <= 99, numbers))


def is_all_has_a(words: list) -> bool:
    """Return True if every word contains 'a' (case-insensitive)."""
    return all(map(lambda w: "a" in w.lower(), words))


def print_with_numbering(items):
    """Print items with 1-based numbering, one per line."""
    for i in range(len(items)):
        print(f"{i + 1}. {items[i]}")


def parallel_print(countries, capitals):
    """Print country - capital pairs, one per line."""
    for i in range(min(len(countries), len(capitals))):
        print(f"{countries[i]} - {capitals[i]}")


def make_dict(keys, values) -> dict:
    """Create a dict by zipping keys and values."""
    return dict(zip(keys, values))


def indices_of_big_words(words) -> list:
    """Return indices of words with length > 5."""
    return list(map(lambda x: x[0], filter(lambda x: len(x[1]) > 5, enumerate(words))))


def decode_rle(chars: str, repeats: list) -> str:
    """Decode run-length encoding: each char repeated by its paired count."""
    return "".join(map(lambda t: t[0] * t[1], zip(chars, repeats)))


# --- driver code ---
if __name__ == "__main__":
    numbers = list(map(int, input("enter numbers (space-separated): ").split()))
    print("is_greater_than_5      :", is_greater_than_5(numbers))
    print("filter_less_than_5     :", filter_less_than_5(numbers))
    print("sum_of_two_digit_numbers:", sum_of_two_digit_numbers(numbers))

    words = input("enter words (space-separated): ").split()
    print("is_all_has_a           :", is_all_has_a(words))
    print("print_with_numbering   :")
    print_with_numbering(words)
    print("indices_of_big_words   :", indices_of_big_words(words))

    countries = input("enter countries (space-separated): ").split()
    capitals  = input("enter capitals  (space-separated): ").split()
    print("parallel_print         :")
    parallel_print(countries, capitals)
    print("make_dict              :", make_dict(countries, capitals))

    chars   = input("enter chars for RLE (no spaces): ")
    repeats = list(map(int, input("enter repeat counts (space-separated): ").split()))
    print("decode_rle             :", decode_rle(chars, repeats))