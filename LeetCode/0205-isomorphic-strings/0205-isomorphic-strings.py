class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}
        mapped = set()

        for char_s,char_t in zip(s,t):
            if char_s in char_map: 
                if char_map[char_s] != char_t:
                    return False
            
            else:
                if char_t in mapped:
                    return False
                char_map[char_s] = char_t
                mapped.add(char_t)
            
        return True
