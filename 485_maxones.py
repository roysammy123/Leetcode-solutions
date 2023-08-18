class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        count = 0
        for i in nums:
            if i==1:
                count += 1
            elif i==0:
                if count > max:
                    max = count
                count = 0
        
        if nums[-1]==1:
            if count>max:
                max = count
        return max
