class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        sums = [0] * len(nums)
        for x in range(len(nums)) :
                sums[x] = sum(int(y) for y in str(nums[x]))
        pairs = list(zip(sums, nums))
        order = sorted(range(len(nums)), key=lambda i: pairs[i])
        visited = [False] * len(nums)
        swaps = 0
        for i in range(len(nums)):
            if visited[i] or order[i] == i:
                continue
            j, length = i, 0
            while not visited[j]:
                visited[j] = True
                j = order[j]
                length += 1
            swaps += length - 1
        return swaps


        