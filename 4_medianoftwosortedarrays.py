class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0

        nums = []

        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        while (i < len(nums1)):
            nums.append(nums1[i])
            i += 1
        while (j < len(nums2)):
            nums.append(nums2[j])
            j += 1
        
        n = len(nums)
        if n % 2 == 0:
            median = nums[(n//2)-1]+nums[(n//2)]
            print(median)
            median = median/2
            return median
        else:
            return nums[(n//2)]
