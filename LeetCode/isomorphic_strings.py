"""
Question: Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t,
where no two characters may map to the same character and mapping is consistent.

Logic: Use a hashmap to track s->t character mappings and a set to track
already mapped t characters, ensuring bijective consistency throughout.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}  # Maps each character in s to its corresponding character in t
        mapped = set()  # Tracks characters in t that are already mapped

        for char_s, char_t in zip(s, t):  # Iterate both strings simultaneously
            if char_s in char_map:
                if char_map[char_s] != char_t:  # Existing mapping contradicts current pair
                    return False
            else:
                if char_t in mapped:  # char_t already mapped to a different char_s
                    return False
                char_map[char_s] = char_t  # Establish new mapping
                mapped.add(char_t)  # Mark char_t as used

        return True