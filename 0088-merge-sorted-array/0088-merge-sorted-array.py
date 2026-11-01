class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        k = m
        for x in nums2:
            nums1[k] = x
            k += 1
        nums1.sort()
        


            
        