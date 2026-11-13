class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #while loop or if condition for 9
        #maybe a function
        #remove 
        if digits[-1]<9:
            digits[-1]+=1
            return digits
        if digits[-1]==9:
            return self.nineUp(digits)
    def nineUp(self,n):
        i=0
        while n and n[-1]==9:
            n.pop()
            i+=1
        if n: 
            n[-1]+=1
        else: 
            n.append(1)
        while i>0:
            n.append(0)
            i-=1
        return n
            