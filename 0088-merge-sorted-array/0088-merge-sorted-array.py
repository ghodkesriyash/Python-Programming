class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for x in nums2:
            y = m-1
            while( y >= 0 and x < nums1[y]):
                nums1[y+1] = nums1[y]
                y -= 1
            nums1[y+1] = x
            m += 1
        


            
        