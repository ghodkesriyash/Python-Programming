
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0

        for right in range(len(s)):
            sub =s[left:right +1]
            while len(sub) != len(set(sub)):
                left += 1
                sub = s[left:right +1]
            longest = max(longest, len(sub))
        return longest


