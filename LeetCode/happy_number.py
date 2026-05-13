# Question: Happy Number
# Determine if a number is "happy". A happy number is defined by the process:
# starting with any positive integer, replace the number by the sum of the squares
# of its digits, and repeat until it either reaches 1 (happy) or loops endlessly
# in a cycle (not happy).
#
# Categories: Math | Hash Set | Recursion

def isHappy(self, n: int, seen=None) -> bool:
    # Initialize the seen set on first call
    # (can't use seen=set() as default — mutable default args are shared across calls)
    if seen is None:
        seen = set()
    
    # Base case: reached 1, number is happy
    if n == 1:
        return True
    
    # Cycle detected: number has appeared before, it will loop forever → not happy
    if n in seen:
        return False
    
    # Mark current number as visited
    seen.add(n)
    
    # Compute sum of squares of digits
    # e.g. 19 → 1² + 9² = 82
    new = sum(int(i) ** 2 for i in str(n))
    
    # Recurse with the new number, passing along the seen set
    return self.isHappy(new, seen)