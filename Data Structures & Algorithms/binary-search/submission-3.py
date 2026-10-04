class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #l,r pointer
        #while loop
        #check for target == mid
        #if target>mid l=mid+1
        #vice versa
        #return mid

        l,r = 0, len(nums)-1
        while l<=r:
            mid = math.floor((l+r)/2)
            if target == nums[mid]:
                return mid
            if target>nums[mid]:
                l=mid+1
            if target<nums[mid]:
                r=mid-1
        
        return -1
