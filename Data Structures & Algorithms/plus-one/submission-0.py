class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #iterate through array
        #either turn to str then int or 
        strDigit =""
        for digit in digits:
            strDigit+=(str(digit))
        
        sum = int(strDigit)+1
        strSum =str(sum)
        newDigits = []
        for i in range(len(strSum),):
            newDigits.append(int(strSum[i]))

        return newDigits
