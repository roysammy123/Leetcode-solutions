class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        list=[]
        n = nums.count(target)
        
        if len(nums)==0 or n==0:
            return [-1,-1]
        elif n==1:
            for i in range(0, len(nums)):
                if nums[i] == target:
                    list.append(i)
                    list.append(i)
                    return list
        else:
            count = 0
            for i in range(0, len(nums)):
                if nums[i]==target:
                    if count==0:
                        list.append(i)
                    elif count==n-1:
                        list.append(i)
                    count += 1
            return list
