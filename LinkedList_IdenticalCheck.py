# your task is to complete this function
# function should return true/1 if both
# are identical else return false/0
'''
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
'''
class Solution:
    #Function to check whether two linked lists are identical or not.
    def areIdentical(self, head1, head2):
        if not head1 and not head2:
            return True
        curr1,curr2=head1,head2
        while curr1 and curr2:
            if curr1.data != curr2.data:
                return False
            curr1=curr1.next
            curr2=curr2.next
        if curr1 or curr2:
            return False
        return True
#{ 
 # Driver Code Starts
# Node Class
# Node Class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):

        arr1 = (int(x) for x in input().split())
        num1 = LinkedList()
        for i in arr1:
            num1.insert(i)

        arr2 = (int(x) for x in input().split())
        num2 = LinkedList()
        for i in arr2:
            num2.insert(i)

        res = Solution().areIdentical(num1.head, num2.head)
        if (res):
            print('true')
        else:
            print('false')
        print("~")
# } Driver Code Ends