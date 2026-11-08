class Solution:
    def toLowerCase(self, s: str) -> str:
        cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lst = list(s)
        for i in range(len(lst)):
            if lst[i] in cap:
                lst[i] = lst[i].lower()
        return "".join(lst)
                                                                            