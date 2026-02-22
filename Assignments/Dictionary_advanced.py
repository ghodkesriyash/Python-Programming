# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : Dictionary Comprehensions & Advanced Dict Operations
# File    : dictionary_advanced.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - Advanced Dictionary Tasks
#
#   total_price(fruit_prices: dict, purchases) -> float
#       Compute total cost of purchases (list of (fruit, quantity) tuples).
#       Do NOT use the sum() function.
#
#   total_price_no_loops(fruit_prices: dict, purchases) -> float
#       Same as above but using sum() and a generator — no loops.
#
#   find_cheapest_fruit(fruit_prices: dict) -> str
#       Return the name of the cheapest fruit. Do NOT use min().
#
#   find_cheapest_fruit_no_loops(fruit_prices: dict) -> str
#       Same as above using min() with a key — no loops.
#
#   group_fruits(fruits: list) -> dict
#       Group fruit names by their first letter (assumed uppercase).
#       Values are lists of fruits sorted ascending.
#       e.g. ["Apple","Avocado","Banana"] → {"A":["Apple","Avocado"],"B":["Banana"]}
#
#   bin_fruits(fruit_prices: dict) -> dict
#       Classify fruits into:
#         cheap      → price < 3
#         affordable → 3 <= price <= 6
#         costly     → price > 6
#       Returns dict with category as key and set of fruit names as value.
# -----------------------------------------------------------------------------


def total_price(fruit_prices: dict, purchases) -> float:
    """Compute total purchase cost without sum(). Manual accumulation."""
    total = 0.0
    for fruit, quantity in purchases:
        total += fruit_prices[fruit] * quantity
    return total


def total_price_no_loops(fruit_prices: dict, purchases) -> float:
    """Compute total purchase cost using sum() and a generator — no loops."""
    return sum(fruit_prices[fruit] * quantity for fruit, quantity in purchases)


def find_cheapest_fruit(fruit_prices: dict) -> str:
    """Return name of cheapest fruit without min(). Manual comparison."""
    cheapest_fruit = None
    cheapest_price = float("inf")
    for fruit, price in fruit_prices.items():
        if price < cheapest_price:
            cheapest_price = price
            cheapest_fruit = fruit
    return cheapest_fruit


def find_cheapest_fruit_no_loops(fruit_prices: dict) -> str:
    """Return name of cheapest fruit using min() with key — no loops."""
    return min(fruit_prices, key=fruit_prices.get)


def group_fruits(fruits: list) -> dict:
    """Group fruits by first letter; values are sorted lists."""
    groups = {}
    for fruit in fruits:
        first_letter = fruit[0]
        if first_letter not in groups:
            groups[first_letter] = []
        groups[first_letter].append(fruit)
    for letter in groups:
        groups[letter].sort()
    return groups


def bin_fruits(fruit_prices: dict) -> dict:
    """Classify fruits into cheap / affordable / costly based on price."""
    binned_fruits = {"cheap": set(), "affordable": set(), "costly": set()}
    for fruit, price in fruit_prices.items():
        if price < 3:
            binned_fruits["cheap"].add(fruit)
        elif price <= 6:                        # already know price >= 3
            binned_fruits["affordable"].add(fruit)
        else:
            binned_fruits["costly"].add(fruit)
    return binned_fruits


# --- driver code ---
if __name__ == "__main__":
    # build fruit_prices dict
    n            = int(input("enter number of fruits: "))
    fruit_prices = {}
    for _ in range(n):
        name, price = input("enter fruit name and price (space-separated): ").split()
        fruit_prices[name] = float(price)

    # total_price
    m         = int(input("enter number of purchases: "))
    purchases = []
    for _ in range(m):
        fruit, qty = input("enter fruit name and quantity: ").split()
        purchases.append((fruit, int(qty)))
    print("total_price          :", total_price(fruit_prices, purchases))
    print("total_price_no_loops :", total_price_no_loops(fruit_prices, purchases))

    # find_cheapest_fruit
    print("cheapest (manual)    :", find_cheapest_fruit(fruit_prices))
    print("cheapest (min)       :", find_cheapest_fruit_no_loops(fruit_prices))

    # group_fruits
    fruits = input("enter fruit names to group (space-separated): ").split()
    print("group_fruits         :", group_fruits(fruits))

    # bin_fruits
    print("bin_fruits           :", bin_fruits(fruit_prices))