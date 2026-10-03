class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        for i in nums1:
            j = nums2.index(i)
            for x in nums2[j:]:
                if x > nums2[j]:
                    result.append(x)
                    break
            else:
                result.append(-1)
        
        return result