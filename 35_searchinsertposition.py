class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        res=0
        if len(nums)==0:
            return 0
        else:
            for i in range(0, len(nums)):
                if(nums[i]==target):
                    res=i
                elif(nums[i] < target):
                    res=i+1
            return res  
