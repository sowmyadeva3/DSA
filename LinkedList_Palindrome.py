#User function Template for python3
'''

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
#Function to check whether the list is palindrome.
class Solution:
    def Reverse(self,head):
        prev = None
        current = head
        while current:
            newNode=Node(current.data)
            newNode.next=prev
            prev=newNode
            current=current.next
        return prev
    def isPalindrome(self, head):
        newHead = self.Reverse(head)
        temp1= head
        temp2 = newHead
        while temp1:
            if temp1.data!=temp2.data:
                return False
            temp1=temp1.next
            temp2=temp2.next
        return True


#{ 
 # Driver Code Starts
#main


class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print("")


if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        values = input().strip().split()
        for i in reversed(values):
            llist.push(i)
        flag = Solution().isPalindrome(llist.head)
        if flag:
            print("true")
        else:
            print("false")
        t -= 1
        print("~")

# } Driver Code Ends

#Optimized version reverse only 2nd half

#User function Template for python3
'''

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
#Function to check whether the list is palindrome.
class Solution:
    def Reverse(self,head):
        prev = None
        current = head
        while current:
            newNode=Node(current.data)
            newNode.next=prev
            prev=newNode
            current=current.next
        return prev
    def isPalindrome(self, head):
        slow,fast = head, head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        secondHalf= slow.next
        newHead = self.Reverse(secondHalf)
        temp1= head
        temp2 = newHead
        while temp2:
            if temp1.data!=temp2.data:
                return False
            temp1=temp1.next
            temp2=temp2.next
        return True


#{ 
 # Driver Code Starts
#main


class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print("")


if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        values = input().strip().split()
        for i in reversed(values):
            llist.push(i)
        flag = Solution().isPalindrome(llist.head)
        if flag:
            print("true")
        else:
            print("false")
        t -= 1
        print("~")

# } Driver Code Ends