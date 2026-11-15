class Solution:
    def hammingWeight(self, n: int) -> int:
        #take bin then right shift and add 1 to res

        res = 0
        while n:
            res += n&1
            n = n>>1
        return res
            