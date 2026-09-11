class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Check if the character is alphanum
        #Cycle through one set comparing the number of times each character appears

        dictS, dictT = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            dictS[s[i]] = 1 + dictS.get(s[i], 0)
            dictT[t[i]] = 1 + dictT.get(t[i], 0)

        return dictT == dictS
        

     