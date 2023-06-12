class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        i = 0
        lenght = len(nums)
        while i < lenght:
            if nums[i] != 0:
                nums[count],nums[i] = nums[i] , nums[count]

                count +=1
            i+=1
        
        
                