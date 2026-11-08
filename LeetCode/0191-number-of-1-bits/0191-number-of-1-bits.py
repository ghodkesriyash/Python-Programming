class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = []
        count = 0
        while n != 0:
            bit = n % 2 
            binary.append(bit)
            n = n // 2
        for x in binary :
            if x == 1:
                count += 1
        return count 