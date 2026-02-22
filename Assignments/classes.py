# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : Object Oriented Programming - Classes & Methods
# File    : classes.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - Basic Calculator Class
#
# Create a Calculator class with two attributes a and b (int).
#
#   __init__(self, a, b)
#       Initialise the calculator with two numbers.
#
#   add(self) -> int
#       Return a + b.
#
#   multiply(self) -> int
#       Return a * b.
#
#   subtract(self) -> int
#       Return a - b.
#
#   quotient(self) -> int
#       Return a // b (integer division).
#
#   remainder(self) -> int
#       Return a % b.
# -----------------------------------------------------------------------------


class Calculator:
    """A class to perform basic arithmetic operations on two numbers."""

    def __init__(self, a, b):
        """Initialise with two numbers a and b."""
        self.a = a
        self.b = b

    def add(self) -> int:
        """Return the sum of a and b."""
        return self.a + self.b

    def multiply(self) -> int:
        """Return the product of a and b."""
        return self.a * self.b

    def subtract(self) -> int:
        """Return a minus b."""
        return self.a - self.b

    def quotient(self) -> int:
        """Return the integer quotient of a divided by b."""
        return self.a // self.b

    def remainder(self) -> int:
        """Return the remainder when a is divided by b."""
        return self.a % self.b


# --- driver code ---
if __name__ == "__main__":
    a   = int(input("enter first number  (a): "))
    b   = int(input("enter second number (b): "))
    cal = Calculator(a, b)

    print("add      :", cal.add())
    print("multiply :", cal.multiply())
    print("subtract :", cal.subtract())
    print("quotient :", cal.quotient())
    print("remainder:", cal.remainder())