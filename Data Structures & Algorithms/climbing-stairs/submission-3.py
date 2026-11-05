class Solution:
    def climbStairs(self, n: int) -> int:
        #no. of solutions = n-1,n-2 until 0
        
        s1,s2 = 1,0

        for i in range(n):
            temp = s1
            s1 = s2+s1
            s2 = temp

        return s1
