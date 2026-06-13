class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        x = int(num1)
        y = int(num2)
        return str(x + y)