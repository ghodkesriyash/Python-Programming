class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)
        result = []
        i = 0
        while i < len(prev):
            j = i
            while j < len(prev) and prev[j] == prev[i]:
                j += 1
            result.append(str(j - i) + prev[i])
            i = j
        return "".join(result)