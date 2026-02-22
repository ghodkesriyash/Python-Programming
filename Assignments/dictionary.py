# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : Dictionary Operations
# File    : dictionary_operations.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - Dictionary Operations
#
#   dictionary_operations(fruit_prices: dict, fruits: list)
#       Perform a series of in-place mutations on fruit_prices and print after
#       each step (via order_print which is defined in hidden evaluator code):
#         - Add fruits[0] with price 3
#         - Update fruits[1] price to 2
#         - Increase fruits[2] price by 2
#         - Delete fruits[3] entry
#         - Print price of fruits[4]
#         - Print all fruit names sorted ascending
#         - Print all prices sorted ascending
#
#   increase_prices(fruit_prices: dict) -> None
#       Increase every fruit's price by 20% and round to 2 decimal places.
#       Modifies dict in-place, returns nothing.
#
#   dict_from_string(string: str, key_type, value_type) -> dict
#       Parse a multiline string of "key,value" pairs into a dictionary.
#       Convert keys and values to the given types.
#
#   dict_to_string(D: dict) -> str
#       Convert a dictionary back to the "key,value" per line string format.
#       Use comprehensions — no loops or conditionals.
# -----------------------------------------------------------------------------


def dictionary_operations(fruit_prices: dict, fruits: list):
    """Perform sequential mutations on fruit_prices, printing after each step."""
    fruit_prices[fruits[0]]  = 3                    # add new fruit with price 3
    order_print(fruit_prices)

    fruit_prices[fruits[1]]  = 2                    # update existing price to 2
    order_print(fruit_prices)

    fruit_prices[fruits[2]] += 2                    # increment existing price by 2
    order_print(fruit_prices)

    del fruit_prices[fruits[3]]                     # delete fruit entry entirely
    order_print(fruit_prices)

    print(fruit_prices[fruits[4]])                  # print price of fruits[4]
    print(sorted(fruit_prices.keys()))              # fruit names ascending
    print(sorted(fruit_prices.values()))            # prices ascending


def increase_prices(fruit_prices: dict) -> None:
    """Increase all prices by 20%, rounded to 2 decimal places. In-place."""
    for fruit in fruit_prices:
        fruit_prices[fruit] = round(fruit_prices[fruit] * 1.2, 2)


def dict_from_string(string: str, key_type, value_type) -> dict:
    """Parse 'key,value' per line string into a typed dictionary."""
    lines = string.strip().split("\n")
    D = {}
    for line in lines:
        if line.strip():                            # skip empty lines
            key, value = line.split(",")
            D[key_type(key.strip())] = value_type(value.strip())
    return D


def dict_to_string(D: dict) -> str:
    """Convert dictionary back to 'key,value' per line string format."""
    return "\n".join([f"{key},{value}" for key, value in D.items()])


# --- driver code ---
if __name__ == "__main__":
    # dictionary_operations — order_print not available outside evaluator,
    # so we substitute with a regular print for local testing
    order_print = lambda d: print(dict(sorted(d.items())))

    n           = int(input("enter number of fruits in price dict: "))
    fruit_prices = {}
    for _ in range(n):
        name, price = input("enter fruit name and price (space-separated): ").split()
        fruit_prices[name] = float(price)

    fruits = input("enter 5 fruit names (space-separated): ").split()
    dictionary_operations(fruit_prices, fruits)

    # increase_prices
    n            = int(input("enter number of fruits for price increase: "))
    fruit_prices = {}
    for _ in range(n):
        name, price = input("enter fruit name and price: ").split()
        fruit_prices[name] = float(price)
    increase_prices(fruit_prices)
    print("increased prices:", fruit_prices)

    # dict_from_string
    print("enter key-value pairs (one per line, comma-separated). Type END to stop:")
    lines = []
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    string    = "\n".join(lines)
    key_type  = str
    value_type = float
    print("dict_from_string:", dict_from_string(string, key_type, value_type))

    # dict_to_string
    D = dict_from_string(string, key_type, value_type)
    print("dict_to_string:\n", dict_to_string(D))