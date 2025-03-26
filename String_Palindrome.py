#User function Template for python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
		i,j=0,len(s)-1
		while i<j:
		    if s[i]!=s[j]:
		        return False
		    i+=1
		    j-=1
	    return True


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()  # Use lowercase 's'
        ob = Solution()
        answer = ob.isPalindrome(s)
        print("true" if answer else "false")  # Print "true" or "false"
        print("~")

# } Driver Code Ends