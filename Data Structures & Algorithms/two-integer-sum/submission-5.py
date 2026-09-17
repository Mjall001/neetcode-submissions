class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #iterate using enumerator
        #save val and index using dictionairy
        #output diff index and n index

        seenMap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in seenMap:
                return [seenMap[diff], i]
            seenMap[n] = i