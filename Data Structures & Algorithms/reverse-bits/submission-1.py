class Solution:
    def reverseBits(self, n: int) -> int:
        #obtain last digit and left shift by corresponding digit posittion

        res=0
        for i in range(31,-1,-1):
            if 1 & n:
                lastDigit = 1&n
                res += (lastDigit<<i)
            n=(n>>1)

        return res