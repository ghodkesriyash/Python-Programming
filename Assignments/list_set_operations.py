# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : List & Set Operations (no loops allowed)
# File    : list_set_operations.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - List Mutating, Non-Mutating & Set Operations (no for/while loops)
#
#   list_mutating_operations(items, item1, item2)
#       Performs in-place mutations on `items` and prints after each step:
#       sort → append item1 → insert item2 at index 3 → extend with first 3
#       → pop 5th element → remove first item2 → set index 4 to None
#       → set even indices to None → delete third last → delete even indices
#       Returns (items, popped_item)
#
#   list_non_mutating_operations(items, item1, item2)
#       Same operations but WITHOUT mutating the original list — each step
#       prints a new list using slicing and concatenation.
#       Returns original items unchanged.
#
#   do_set_operation(set1, set2, set3, item1, item2)
#       add item1 to set1
#       discard item2 from set1 (no error if missing)
#       update set1 with set2
#       remove from set1 all elements in set3
#       print intersection of set2 & set3
#       print union of set1, set2, set3
#       print set2 - set3 (difference)
#       print set2 △ set3 (symmetric difference)
#       Returns (set1, sorted(set1), sorted(set2), sorted(set3))
# -----------------------------------------------------------------------------

# Note: the self-referencing prefix checker is omitted (not needed standalone).


def list_mutating_operations(items: list, item1, item2):
    items.sort()
    print("sorted:", items)

    items.append(item1)
    print("append:", items)

    items.insert(3, item2)
    print("insert:", items)

    items.extend(items[:3])
    print("extend:", items)

    popped_item = items.pop(4)
    print("pop:", items)

    items.remove(item2)
    print("remove:", items)

    items[4] = None
    print("modify_index:", items)

    items[::2] = [None] * len(items[::2])   # set all even-index slots to None
    print("modify_slice:", items)

    del items[-3]                            # delete third last element
    print("delete_index:", items)

    del items[::2]                           # delete all even-index slots
    print("delete_slice:", items)

    return items, popped_item


def list_non_mutating_operations(items: list, item1, item2):
    print("sorted:", sorted(items))

    print("append:", items + [item1])

    print("insert:", items[:3] + [item2] + items[3:])

    print("extend:", items + items[:3])

    print("pop:", items[:4] + items[5:])     # skip index 4 (5th element)

    idx = items.index(item2)                 # index of first occurrence of item2
    print("remove:", items[:idx] + items[idx + 1:])

    print("modify_index:", items[:3] + [None] + items[4:])

    modified_list       = items[:]
    modified_list[::2]  = [None] * len(modified_list[::2])
    print("modify_slice:", modified_list)

    print("delete_slice:", items[1::2])      # keep only odd-index elements

    return items


def do_set_operation(set1, set2, set3, item1, item2):
    set1.add(item1)
    print(sorted(set1))

    set1.discard(item2)                      # discard: no error if item2 absent
    print(sorted(set1))

    set1.update(set2)                        # add all elements of set2 to set1
    print(sorted(set1))

    set1.difference_update(set3)             # remove from set1 anything in set3
    print(sorted(set1))

    print(sorted(set2.intersection(set3)))          # common elements in set2 & set3
    print(sorted(set1.union(set2).union(set3)))     # all unique elements across all 3
    print(sorted(set2.difference(set3)))            # in set2 but not in set3
    print(sorted(set2.symmetric_difference(set3)))  # non-common elements of set2 & set3

    return set1, sorted(set1), sorted(set2), sorted(set3)