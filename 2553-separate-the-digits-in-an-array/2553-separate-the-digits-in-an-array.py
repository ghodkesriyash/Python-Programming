class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        temp = []
        for i in nums:
            i = str(i)
            for x in range(len(i)):
                temp.append(int(i[x]))
        return temp