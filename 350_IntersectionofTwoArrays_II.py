class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in nums1:
            if nums2.count(i) >= 1:
                l.append(i)
                nums2.remove(i)
        return l
