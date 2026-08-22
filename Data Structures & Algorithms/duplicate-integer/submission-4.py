class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:       
       #Array A == Array B output True
       #Put Array A elements in set(hashmap could be used but waste of memory)
       #Iterate over Array B if A[i] == B[i] return true
       duplicateChecker = set()
       #print(range(len(nums)))
       
       for i in range(len(nums)):
        #print("this is the ", str(i), "RUN")
        
        if nums[i] in duplicateChecker:
            return True
        duplicateChecker.add(nums[i])
       return False
        #print(str(duplicateChecker))
    
            
        #print("This is happening" +str(duplicateChecker)+"times")