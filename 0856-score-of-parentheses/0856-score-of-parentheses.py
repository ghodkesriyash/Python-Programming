class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        if s == "()":
            return 1                                   # your base case
        bal = 0
        for i, ch in enumerate(s):
            bal += 1 if ch == "(" else -1
            if bal == 0:                               # first balanced chunk ends here
                if i == len(s) - 1:                    # one wrapper: "(" + inner + ")"
                    return 2 * self.scoreOfParentheses(s[1:-1])   # your score *= 2
                return (self.scoreOfParentheses(s[:i + 1])
                        + self.scoreOfParentheses(s[i + 1:]))     # siblings add