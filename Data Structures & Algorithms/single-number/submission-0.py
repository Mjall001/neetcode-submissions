class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #use ord they will cancel out 1s
        res = 0
        for i in nums:
            res ^=i
        return res