class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda l: l[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        res = [0] * len(queries)
        count = {}
        active = 0
        left = right = 0
        L = len(logs)

        for i in order:
            q = queries[i]

            # add logs with time <= q
            while right < L and logs[right][1] <= q:
                s = logs[right][0]
                count[s] = count.get(s, 0) + 1
                if count[s] == 1:
                    active += 1
                right += 1

            # remove logs with time < q - x
            while left < right and logs[left][1] < q - x:
                s = logs[left][0]
                count[s] -= 1
                if count[s] == 0:
                    active -= 1
                left += 1

            res[i] = n - active
        return res