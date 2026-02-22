# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : Functions with Dictionaries - Grocery List
# File    : grocery_list.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - Process Grocery List
#
#   process_grocery_list(grocery_list: list[dict], request: str)
#
#   Args:
#       grocery_list: list of dicts with keys "name", "quantity", "price"
#                     where price is the cost per unit.
#       request (str): one of the following:
#           "total_bill_amount"   → return total cost (sum of quantity * price)
#           "max_quantity_item"   → return name of item with highest quantity
#           "sort_by_total_amount"→ return list sorted by total item cost
#                                   (descending), with name as tiebreaker (asc)
# -----------------------------------------------------------------------------


def process_grocery_list(grocery_list: list, request: str):
    """Process a grocery list based on the given request."""

    if request == "total_bill_amount":
        return sum(i["quantity"] * i["price"] for i in grocery_list)

    if request == "max_quantity_item":
        return max(grocery_list, key=lambda i: i["quantity"])["name"]

    if request == "sort_by_total_amount":
        return sorted(
            grocery_list,
            key=lambda item: (-(item["price"] * item["quantity"]), item["name"])
        )


# --- driver code ---
if __name__ == "__main__":
    n            = int(input("enter number of grocery items: "))
    grocery_list = []
    for _ in range(n):
        name     = input("enter item name: ")
        quantity = int(input(f"enter quantity of {name}: "))
        price    = float(input(f"enter price per unit of {name}: "))
        grocery_list.append({"name": name, "quantity": quantity, "price": price})

    print("total_bill_amount    :", process_grocery_list(grocery_list, "total_bill_amount"))
    print("max_quantity_item    :", process_grocery_list(grocery_list, "max_quantity_item"))
    print("sort_by_total_amount :")
    for item in process_grocery_list(grocery_list, "sort_by_total_amount"):
        print(" ", item)