class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # val:index dict
        # two pointers
        # 4 variabels: diff,target, pointera, pointerb,

        seenNums={}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in seenNums:
                return[seenNums[diff], i]
            
            seenNums[n] = i

            