# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : List Comprehensions
# File    : list_comprehensions.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - List Comprehension Tasks
#
#   sum_of_squares(numbers)
#       Return the sum of squares of all numbers in the list.
#       e.g. [1,2,3] → 1+4+9 = 14
#
#   total_cost(cart)
#       Given a list of (quantity, price) tuples, return the total cost.
#       e.g. [(2,5),(3,10)] → 2*5 + 3*10 = 40
#
#   abbreviation(sentence)
#       Return the dot-separated uppercase initials of each word + trailing dot.
#       e.g. "hello world" → "H.W."
#
#   palindromes(words)
#       Return a list of words that are palindromes.
#       e.g. ["racecar","hello","level"] → ["racecar","level"]
#
#   all_chars_from_big_words(sentence)
#       Return a set of unique lowercase characters from words longer than 5 chars.
#
#   flatten(lol)
#       Flatten a list of lists into a single list.
#
#   unflatten(items, n_rows)
#       Reshape a flat list into a 2D list with n_rows rows.
#       e.g. [1..6], n_rows=2 → [[1,2,3],[4,5,6]]
#
#   make_identity_matrix(m)
#       Return an m×m identity matrix (1s on diagonal, 0s elsewhere).
#
#   make_lower_triangular_matrix(m)
#       Return an m×m lower triangular matrix where entry [i][j] = j+1 if j<=i
#       else 0.
# -----------------------------------------------------------------------------


def sum_of_squares(numbers):
    """Return sum of squares of all numbers."""
    return sum([x ** 2 for x in numbers])


def total_cost(cart):
    """Return total cost from a list of (quantity, price) tuples."""
    return sum([quantity * price for quantity, price in cart])


def abbreviation(sentence):
    """Return dot-separated uppercase initials with trailing dot."""
    return ".".join([word[0].upper() for word in sentence.split()]) + "."


def palindromes(words):
    """Return list of words that read the same forwards and backwards."""
    return [word for word in words if word == word[::-1]]


def all_chars_from_big_words(sentence):
    """Return set of unique lowercase chars from words with more than 5 characters."""
    return set([char.lower() for word in sentence.split()
                for char in word if len(word) > 5])


def flatten(lol):
    """Flatten a list of lists into a single flat list."""
    return [item for sublist in lol for item in sublist]


def unflatten(items, n_rows):
    """Reshape flat list into 2D list with n_rows rows."""
    n_cols = len(items) // n_rows
    return [[items[i * n_cols + j] for j in range(n_cols)] for i in range(n_rows)]


def make_identity_matrix(m):
    """Return m×m identity matrix."""
    return [[1 if i == j else 0 for j in range(m)] for i in range(m)]


def make_lower_triangular_matrix(m):
    """Return m×m lower triangular matrix with entry j+1 if j<=i else 0."""
    return [[(j + 1) * (j <= i) for j in range(m)] for i in range(m)]


# --- driver code ---
if __name__ == "__main__":
    # sum_of_squares
    numbers = list(map(int, input("enter numbers (space-separated): ").split()))
    print("sum_of_squares    :", sum_of_squares(numbers))

    # total_cost
    n    = int(input("enter number of cart items: "))
    cart = [tuple(map(int, input("enter quantity price: ").split())) for _ in range(n)]
    print("total_cost        :", total_cost(cart))

    # abbreviation
    sentence = input("enter sentence for abbreviation: ")
    print("abbreviation      :", abbreviation(sentence))

    # palindromes
    words = input("enter words (space-separated): ").split()
    print("palindromes       :", palindromes(words))

    # all_chars_from_big_words
    sentence = input("enter sentence for big word chars: ")
    print("big word chars    :", all_chars_from_big_words(sentence))

    # flatten
    n   = int(input("enter number of sublists: "))
    lol = [list(map(int, input(f"enter sublist {i+1} (space-separated): ").split()))
           for i in range(n)]
    print("flatten           :", flatten(lol))

    # unflatten
    items  = list(map(int, input("enter flat list (space-separated): ").split()))
    n_rows = int(input("enter number of rows: "))
    print("unflatten         :", unflatten(items, n_rows))

    # make_identity_matrix
    m = int(input("enter matrix size for identity matrix: "))
    print("identity_matrix   :", make_identity_matrix(m))

    # make_lower_triangular_matrix
    m = int(input("enter matrix size for lower triangular matrix: "))
    print("lower_triangular  :", make_lower_triangular_matrix(m))