class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        x = 0
        mini = 200
        for i in strs:
            if len(i) < mini:
                mini = len(i)
        while x < mini:
            curr = strs[0][x]
            for i in strs:
                if i[x] != curr:
                    return pre
            pre += curr
            x += 1
        return pre
