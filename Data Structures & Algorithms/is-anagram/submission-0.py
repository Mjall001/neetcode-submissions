class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Check if they're the same length
        #iterate through word
        #Add letters to hashmap and compare count

        if len(s) != len(t):
            return False

        validAna ={}

        for i in range(len(s)):
            validAna[s[i]] = 1 + validAna.get(s[i], 0)
            validAna[t[i]] = -1 + validAna.get(t[i], 0)

        for i in validAna.values():
            if i != 0:
                return False
        return True
        