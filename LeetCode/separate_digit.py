"""
Question: Separate the Digits in an Array
Given an array of positive integers, return an array of the individual
digits of each integer in the same order they appear.

Categories: Array | Simulation
"""

def separateDigits(self, nums: List[int]) -> List[int]:
    """
    Approach: String Conversion
    Convert each number to a string, iterate over each character,
    convert back to int and append to result list.
    """

    temp = []

    for i in nums:
        """ Convert number to string to access individual digits """
        i = str(i)

        """ Append each digit as an integer to the result list """
        for x in range(len(i)):
            temp.append(int(i[x]))

    return temp