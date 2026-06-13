from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        maps = {2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"],}
        final=[]
        elements = [maps[int(d)] for d in digits]

        for combo in product(*elements):
            final.append("".join(combo))
        return final

