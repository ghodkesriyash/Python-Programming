# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : List Slicing & Rotation Functions
# File    : list_slicing_functions.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - List Manipulation via Slicing
#
#   swap_halves(items)
#       Return a new list with the two halves swapped.
#       e.g. [1,2,3,4] → [3,4,1,2]
#
#   swap_at_index(items, k)
#       Split the list at index k (inclusive) and swap the two parts.
#       e.g. [1,2,3,4,5], k=2 → [4,5,1,2,3]
#
#   rotate_k(items, k=1)
#       Rotate the list right by k positions (last k elements move to front).
#       Handles k larger than list length via modulo.
#       e.g. [1,2,3,4,5], k=2 → [4,5,1,2,3]
#
#   first_and_last_index(items, elem)
#       Return a tuple (first_index, last_index) of elem in items.
#
#   reverse_first_and_last_halves(items)
#       Reverse the first half and the second half of items IN-PLACE.
#       e.g. [1,2,3,4,5,6] → [3,2,1,6,5,4]
# -----------------------------------------------------------------------------


def swap_halves(items):
    """Return new list with first and second halves swapped."""
    mid = len(items) // 2
    return items[mid:] + items[:mid]


def swap_at_index(items, k):
    """Split at index k (inclusive) and swap the two parts."""
    return items[k + 1:] + items[:k + 1]


def rotate_k(items, k=1):
    """Rotate list right by k positions. Last k elements move to the front."""
    if not items:
        return items
    k = k % len(items)          # handle k > len(items)
    return items[-k:] + items[:-k]


def first_and_last_index(items, elem):
    """Return (first_index, last_index) of elem in items."""
    indexes = [i for i in range(len(items)) if items[i] == elem]
    return (indexes[0], indexes[-1])


def reverse_first_and_last_halves(items):
    """Reverse first half and second half of items in-place."""
    mid          = len(items) // 2
    items[:mid]  = items[:mid][::-1]
    items[mid:]  = items[mid:][::-1]