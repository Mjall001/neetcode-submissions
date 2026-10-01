class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #use l and r to get lower and upper bound
        #calculate mid using floor((l+r)/2)
        #restructure if bigger by moving l to mid-1
        #restructure if smaller by moving r =mind+1

        l,r = 0, len(nums)-1

        while l<=r:
            mid = math.floor((l+r)/2)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1