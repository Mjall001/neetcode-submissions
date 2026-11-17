class Solution:
    def isHappy(self, n: int) -> bool:
        #function to calculate sum of squares
        #slow and fast pointer
        #break when they equal each other
        #return true if 1 false if not
        slow = self.sumSquares(n)
        fast = self.sumSquares(slow)
        while fast != slow:
            slow = self.sumSquares(slow)
            fast = self.sumSquares(fast)
            fast = self.sumSquares(fast)

        if slow != 1:
            return False
        return True
    def sumSquares(self,n):
        res = 0

        while n:#runs until less than 10
            res += (n%10)**2
            n = n//10
        return res