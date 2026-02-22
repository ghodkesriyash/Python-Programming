# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : 2D Matrix / Grid Traversal
# File    : matrix_traversal.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - 2D Matrix Path Operations
#
# Given a 2D matrix M containing 0s and 1s that form a connected path:
#
#   index_of_first_occurance(row: list, elem)
#       Return index of first occurrence of elem in row, or -1 if not found.
#
#   index_of_last_occurance(row: list, elem)
#       Return index of last occurrence of elem in row, or -1 if not found.
#
#   is_valid_coordinate(x, y, M)
#       Return True if (x, y) is within the bounds of matrix M.
#
#   valid_adjacent_coordinates(x, y, M)
#       Return a set of valid (up/down/left/right) neighbour coordinates of (x,y).
#
#   next_coordinate_with_value(curr_coords, value, M, prev_coords=None)
#       Return the first adjacent coordinate (excluding prev_coords) whose
#       cell equals `value`. Returns None if no such neighbour exists.
#
#   get_path_coordinates(M)
#       Trace the full path of 1s starting from the last 1 in the bottom row.
#       Returns list of (x, y) coordinate tuples along the path.
#
#   print_path(M)
#       Print each coordinate in the path (top to bottom traversal order).
#
#   alternate_path(M)
#       Modify M in-place: alternating path cells get values 2 and 1
#       (starting from the END of the path — 2, 1, 2, 1...).
#
#   count_path(M)
#       Modify M in-place: replace each path cell with its step number
#       (1-indexed, starting from the beginning of the path).
#
#   mirror_horizontally(M)
#       For each (x, y) on the path, set M[x][n_cols-1-y] = 1 (horizontal mirror).
#
#   mirror_vertically(M)
#       For each (x, y) on the path, set M[n_rows-1-x][y] = 1 (vertical mirror).
# -----------------------------------------------------------------------------


def index_of_first_occurance(row: list, elem):
    """Return index of first occurrence of elem in row, -1 if absent."""
    for i in range(len(row)):
        if row[i] == elem:
            return i
    return -1


def index_of_last_occurance(row: list, elem):
    """Return index of last occurrence of elem in row, -1 if absent."""
    reversed_row      = row[::-1]
    first_in_reversed = index_of_first_occurance(reversed_row, elem)
    if first_in_reversed == -1:
        return -1
    return len(row) - 1 - first_in_reversed


def is_valid_coordinate(x: int, y: int, M):
    """Return True if (x, y) lies within the bounds of matrix M."""
    return 0 <= x < len(M) and 0 <= y < len(M[0])


def valid_adjacent_coordinates(x: int, y: int, M):
    """Return set of valid up/down/left/right neighbours of (x, y) in M."""
    return {
        (x1, y1)
        for x1, y1 in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        if is_valid_coordinate(x1, y1, M)
    }


def next_coordinate_with_value(curr_coords, value, M, prev_coords=None):
    """Return first adjacent coord (not prev_coords) whose cell equals value."""
    x, y       = curr_coords
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]   # up, left, right, down
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if (is_valid_coordinate(nx, ny, M)
                and M[nx][ny] == value
                and (nx, ny) != prev_coords):
            return (nx, ny)
    return None


def get_path_coordinates(M):
    """Trace path of 1s from the last 1 in the bottom row. Returns coord list."""
    x_start = len(M) - 1
    y_start = index_of_last_occurance(M[-1], 1)
    if y_start == -1:
        return []
    path        = []
    curr_coords = (x_start, y_start)
    prev_coords = None
    while curr_coords is not None:
        path.append(curr_coords)
        next_coords = next_coordinate_with_value(curr_coords, 1, M, prev_coords)
        prev_coords = curr_coords
        curr_coords = next_coords
    return path


def print_path(M):
    """Print each (x, y) coordinate along the path of 1s."""
    path = get_path_coordinates([row[:] for row in M])
    for coord in path:
        print(coord)


def alternate_path(M):
    """Mark path in reverse: alternating cells become 2 and 1 (2 first)."""
    path = get_path_coordinates([row[:] for row in M])
    path.reverse()
    for i, (x, y) in enumerate(path):
        M[x][y] = 2 if i % 2 == 0 else 1


def count_path(M):
    """Replace each path cell with its 1-indexed step number."""
    path = get_path_coordinates([row[:] for row in M])
    for i, (x, y) in enumerate(path):
        M[x][y] = i + 1


def mirror_horizontally(M):
    """Set M[x][n_cols-1-y] = 1 for each (x,y) on the path."""
    path   = get_path_coordinates([row[:] for row in M])
    n_cols = len(M[0])
    for x, y in path:
        M[x][n_cols - 1 - y] = 1


def mirror_vertically(M):
    """Set M[n_rows-1-x][y] = 1 for each (x,y) on the path."""
    path   = get_path_coordinates([row[:] for row in M])
    n_rows = len(M)
    for x, y in path:
        M[n_rows - 1 - x][y] = 1


# --- driver code ---
if __name__ == "__main__":
    n_rows = int(input("enter number of rows: "))
    M      = []
    for i in range(n_rows):
        row = list(map(int, input(f"enter row {i + 1} (space-separated): ").split()))
        M.append(row)

    print("\n--- print_path ---")
    print_path(M)

    import copy
    M_alt = copy.deepcopy(M)
    alternate_path(M_alt)
    print("\n--- alternate_path ---")
    for row in M_alt: print(row)

    M_count = copy.deepcopy(M)
    count_path(M_count)
    print("\n--- count_path ---")
    for row in M_count: print(row)

    M_mh = copy.deepcopy(M)
    mirror_horizontally(M_mh)
    print("\n--- mirror_horizontally ---")
    for row in M_mh: print(row)

    M_mv = copy.deepcopy(M)
    mirror_vertically(M_mv)
    print("\n--- mirror_vertically ---")
    for row in M_mv: print(row)