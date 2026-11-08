class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        size = len(nums1)
        k = k1 + k2

        diffs = [abs(nums1[i] - nums2[i]) for i in range(size)]
        max_diff = max(diffs)

        cnt = [0] * (max_diff + 1)
        for d in diffs:
            cnt[d] += 1

        for v in range(max_diff, 0, -1):
            if cnt[v] == 0:
                continue
            if k >= cnt[v]:
                k -= cnt[v]
                cnt[v - 1] += cnt[v]
                cnt[v] = 0
            else:
                cnt[v] -= k
                cnt[v - 1] += k
                k = 0
                break

        return sum(v * v * cnt[v] for v in range(max_diff + 1))