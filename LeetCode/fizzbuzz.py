"""
Question: Given an integer n, return a string array answer where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5,
answer[i] == "Fizz" if i is divisible by 3,
answer[i] == "Buzz" if i is divisible by 5,
answer[i] == i (as string) otherwise.

Logic: Preallocate result array, iterate 1 to n, check divisibility conditions
in order of priority (FizzBuzz first) and assign the corresponding string.
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [None] * n  # Preallocate result array of size n
        for i in range(1, n + 1):
            if (i % 3 == 0) and (i % 5 == 0):  # Check FizzBuzz first to avoid partial matches
                answer[i-1] = "FizzBuzz"
            elif (i % 3 == 0):
                answer[i-1] = "Fizz"
            elif (i % 5 == 0):
                answer[i-1] = "Buzz"
            else:
                answer[i-1] = str(i)  # Convert integer to string for non-fizzbuzz cases
        return answer