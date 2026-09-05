class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = set()

        for num in range(len(nums)):
            if nums[num] in dupes:
                return True
            dupes.add(nums[num])

        return False
            
        