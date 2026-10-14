class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        nines,rem = divmod(sum, 9)
        result = "9" * nines
        if rem:
            result += str(rem)
        return result + "0" * (num - len(result))
            