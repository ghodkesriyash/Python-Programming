# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : Collections & Iterables (no for loops allowed)
# File    : collections_iterables.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - Collections & Iterables (for loops are NOT allowed)
#
# Given the following pre-defined variables:
#   int_iterable      = range(1, 10, 3)
#   string_iterable   = ["Apple", "Orange", "Banana"]
#   some_value        = 4
#   some_collection   = [1, 2, 3]       # list | set | tuple
#   some_iterable     = (1, 2, 3)
#   another_iterable  = {"apple", "banana", "cherry"}
#   yet_another_iterable = range(1, 10)
#
# Tasks:
#   - Create empty and singleton versions of list, set, tuple
#   - Create falsy list/set and truthy tuple
#   - Find min, max, sum, len, sorted (asc & desc), reversed of int_iterable
#   - Handle non-reversible iterables gracefully using hasattr checks
#   - Get third last element and odd-index elements of some_collection
#     (None if not indexable/slicable)
#   - Check membership of some_value in some_collection and in even indices
#     (None if not ordered)
#   - Concatenate some_iterable, another_iterable, yet_another_iterable into a list
#   - Join string_iterable with '-'; sort first if not ordered
# -----------------------------------------------------------------------------

# Note: the self-referencing prefix checker is omitted (not needed standalone).

int_iterable         = range(1, 10, 3)
string_iterable      = ["Apple", "Orange", "Banana"]
some_value           = 4
some_collection      = [1, 2, 3]
some_iterable        = (1, 2, 3)
another_iterable     = {"apple", "banana", "cherry"}
yet_another_iterable = range(1, 10)

# --- empty & singleton collections ---
empty_list      = []
empty_set       = set()       # set() not {} — {} creates an empty dict
empty_tuple     = ()
singleton_list  = [0]
singleton_set   = {0}
singleton_tuple = (0,)        # trailing comma makes it a tuple, not just parentheses

# --- falsy and truthy collections ---
a_falsy_list   = []           # empty list  → bool([])   == False
a_falsy_set    = set()        # empty set   → bool(set()) == False
a_truthy_tuple = (1,)         # non-empty   → bool((1,)) == True

# --- int_iterable aggregations ---
int_iterable_min        = min(int_iterable)
int_iterable_max        = max(int_iterable)
int_iterable_sum        = sum(int_iterable)
int_iterable_len        = len(int_iterable)
int_iterable_sorted     = sorted(int_iterable)                  # ascending
int_iterable_sorted_desc = sorted(int_iterable, reverse=True)   # descending

# reversed() only works on sequences that support __reversed__
if hasattr(int_iterable, "__reversed__"):
    int_iterable_reversed = list(reversed(int_iterable))
else:                                                            # fallback: sort desc
    int_iterable_reversed = sorted(int_iterable, reverse=True)

# --- indexing & slicing (only if collection supports it) ---
if hasattr(some_collection, "__getitem__"):
    third_last_element = some_collection[-3]        # third from the end
else:
    third_last_element = None

if hasattr(some_collection, "__getitem__"):
    odd_index_elements = some_collection[1::2]      # elements at indices 1, 3, 5...
else:
    odd_index_elements = None

# --- membership checks ---
is_some_value_in_some_collection = bool(some_value in some_collection)

if hasattr(some_collection, "__getitem__"):
    is_some_value_in_even_indices = some_value in some_collection[::2]  # indices 0, 2, 4...
else:
    is_some_value_in_even_indices = None

# --- concatenate all iterables into one list ---
all_iterables = list(some_iterable) + list(another_iterable) + list(yet_another_iterable)

# --- join string_iterable with '-' (sort first if unordered) ---
if hasattr(string_iterable, "__getitem__"):
    all_concat = "-".join(string_iterable)
else:
    all_concat = "-".join(sorted(string_iterable))