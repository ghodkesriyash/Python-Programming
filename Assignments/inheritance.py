# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : Object Oriented Programming - Inheritance
# File    : inheritance.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - Shape Inheritance
#
# Create a base class Shape and a derived class Square.
#
#   Shape.__init__(self, name)
#       Initialise with name (str). Set area and perimeter to None.
#
#   Shape.display(self)
#       Print: "<name> has an area of <area> and perimeter of <perimeter>"
#
#   Square(Shape)
#       Inherits from Shape.
#
#   Square.__init__(self, side)
#       Call Shape.__init__ with name "Square".
#       Store side, then compute area and perimeter by calling their methods.
#
#   Square.compute_area(self)
#       Set self.area = side * side.
#
#   Square.compute_perimeter(self)
#       Set self.perimeter = 4 * side.
# -----------------------------------------------------------------------------


class Shape:
    """Base class representing a generic shape."""

    def __init__(self, name: str):
        """Initialise shape with a name; area and perimeter start as None."""
        self.name      = name
        self.area      = None
        self.perimeter = None

    def display(self):
        """Print the shape's name, area, and perimeter."""
        print(f"{self.name} has an area of {self.area} and perimeter of {self.perimeter}")


class Square(Shape):
    """A square shape derived from Shape."""

    def __init__(self, side):
        """Initialise Square with side length; compute area and perimeter."""
        super().__init__("Square")
        self.side = side
        self.compute_area()
        self.compute_perimeter()

    def compute_area(self):
        """Set area = side²."""
        self.area = self.side * self.side

    def compute_perimeter(self):
        """Set perimeter = 4 × side."""
        self.perimeter = 4 * self.side


# --- driver code ---
if __name__ == "__main__":
    side = float(input("enter side length of square: "))
    sq   = Square(side)
    sq.display()