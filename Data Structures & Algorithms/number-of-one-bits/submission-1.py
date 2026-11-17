class Solution:
    def hammingWeight(self, n: int) -> int:
        #flip bits by & with -1 and count how many times it happens
        #right shift bits by 1 and count until 0
        res = 0

        while n:
            n &=n-1
            res +=1
        return res