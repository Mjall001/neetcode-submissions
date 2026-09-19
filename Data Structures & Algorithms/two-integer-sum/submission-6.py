class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #two pointers
        #return index positions
        #dictionary to store val and index
        #use dicts getValue for index
        #use diff
        #check if you've seen n before

        seenMap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in seenMap:
                return [seenMap[diff], i]
            seenMap[n] = i