class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Create a set, iterate until i find a value that matches value in set
        
        dupes = set()

        for i in nums:
            if i in dupes:
                return True
            dupes.add(i)

        return False