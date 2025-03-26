class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(0,len(s)):
            rotatedString = s[i:len(s)]+s[0:i]
            
            if rotatedString == goal:
                return True
        return False