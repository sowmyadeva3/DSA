#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        reversedString=""
        for char in s:
            reversedString = char+reversedString
        return reversedString


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        s = input()
        ob = Solution()
        print(ob.reverseString(s))
        t = t - 1

        print("~")

# } Driver Code Ends