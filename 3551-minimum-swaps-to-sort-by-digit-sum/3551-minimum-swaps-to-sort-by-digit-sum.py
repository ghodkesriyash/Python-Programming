class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        size = len(nums)
        sums = [0] * size
        for x in range(size) :
                sums[x] = sum(int(y) for y in str(nums[x]))
        pairs = list(zip(sums, nums))
        order = sorted(range(size), key=lambda i: pairs[i])
        visited = [False] * size
        swaps = 0
        for i in range(size):
            if visited[i] or order[i] == i:
                continue
            j, length = i, 0
            while not visited[j]:
                visited[j] = True
                j = order[j]
                length += 1
            swaps += length - 1
        return swaps


        