class Solution:
    def isPalindrome(self, s: str) -> bool:
        flag = False
        alphanumeric = "abcdefghijklmnopqrstuvwxyz1234567890"
        temp = [i for i in s.lower() if i in alphanumeric]
        s1 = "".join(temp)
        rev = temp[::-1]
        s2 = "".join(rev)
        if s1 == s2 or s == " ":
            flag = True
        return flag