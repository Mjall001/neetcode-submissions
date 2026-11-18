class Solution:
    def countBits(self, n: int) -> List[int]:
        #function to count bits
        #append return to array
        #for i in range
        binCount =[]

        for i in range(0,n+1):
            result=self.count(i)
            binCount.append(result)

        return binCount

    def count(self,n):
        res = 0

        while n:
            res+=1
            n&=n-1
        return res