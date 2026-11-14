class Solution:
    def countBits(self, n: int) -> List[int]:
        #bit patterns 0-4 are repeated by adding 1 from 2pos below
        #every 4 positions this increase by 2
        #for loop that starts from 0 bin(0) to bin(n) use 4 as a
        #benchmark to increase offset
        #start at end of array work backwards
        #helper function to count bits

        offset = n//4
        limit = offset*2
        bitNum=[]
        for i in range(0,n+1):
            bitNum.append(self.sumOfBits(i))

        return bitNum

    def sumOfBits(self,n):
        sum=0
        while n and n>1:
            sum += n%2
            n=n//2
        if n==1:
            sum +=1

        return sum
    