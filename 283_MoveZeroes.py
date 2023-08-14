class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zerocount = nums.count(0)
        index = 0
        for i in nums:
            if i != 0:
                nums[index] = i
                index += 1
        for i in range(zerocount):
            nums[index] = 0
            index += 1
        return nums
