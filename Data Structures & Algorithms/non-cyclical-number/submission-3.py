class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.sumSquares(n)
        fast = self.sumSquares(slow)
        while fast != slow:
            fast = self.sumSquares(fast)
            fast = self.sumSquares(fast)
            slow = self.sumSquares(slow)
        
        return False if slow != 1 else True
    def sumSquares(self,n):
        res = 0

        while n:
            res += (n%10)**2
            n = n//10
        return res