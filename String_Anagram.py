#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        if len(s1)!=len(s2):
            return False
        frequencyArr = [0]*257
        for char in s1:
            frequencyArr[ord(char)]+=1
        for char in s2:
            frequencyArr[ord(char)]-=1
        for i in range(0,len(frequencyArr)):
            if frequencyArr[i]!=0:
                return False
        return True
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = input().strip()
        b = input().strip()
        if (Solution().areAnagrams(a, b)):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends