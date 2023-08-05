class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twosumlist = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    twosumlist.append(i)
                    twosumlist.append(j)
                    break
        
        return twosumlist
