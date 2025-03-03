def isPalindrome(self, n):
        originalNum = n
        newNum = 0
		while n>0:
		    ld = n % 10
		    newNum = (newNum*10) + ld
		    n = n//10
        if originalNum == newNum:
            return True
        else:
            return False