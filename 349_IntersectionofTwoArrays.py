class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in nums1:
            if nums2.count(i) >=1:
                if i not in l:
                    l.append(i)
        return l
