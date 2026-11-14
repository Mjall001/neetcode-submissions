class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #use xor and for i in range, if it doesn't match output it

        nums.sort()
        for i in range(len(nums)):
            if i^nums[i] != 0:
                return i
            
        return 1 + nums[-1] 
            