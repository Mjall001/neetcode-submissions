class Solution:
    def countBits(self, n: int) -> List[int]:
        #offset that multiplies by 2 every time a multiple of 4 
        #2->4->8->16
        #output array,forloop

        df=[0]*(n+1)
        offset=1
        for i in range(1,n+1):
            if offset*2==i:
                offset=i
            df[i]= 1 + df[i-offset]

        return df