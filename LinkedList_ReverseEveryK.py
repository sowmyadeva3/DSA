"""Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""
class Solution:
    def reverse(self,head):
        prev=None
        curr=head
        while curr:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
        return prev
    def reverseKGroup(self, head, k):
        if not head or k==1:
            return head
        currGroupHead,temp=head,head
        newHead=None
        while temp:
            count=1
            while count<k and temp.next:
                temp=temp.next
                count+=1
            
            nextGroupHead =temp.next
            temp.next=None
            
            if not newHead:
                newHead=self.reverse(currGroupHead)
            else:
                
                lastTail.next=self.reverse(currGroupHead)
            lastTail=currGroupHead
            currGroupHead.next=nextGroupHead
            currGroupHead=nextGroupHead
            temp=currGroupHead
        return newHead
            


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


if __name__ == '__main__':
    t = int(input())  # Number of test cases
    while t > 0:
        llist = LinkedList()

        # Read list values and push them to the LinkedList
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)

        k = int(input())  # Size of the group for reversal
        ob = Solution()
        new_head = ob.reverseKGroup(llist.head, k)
        llist.head = new_head
        llist.printList()  # Print the modified linked list
        t -= 1

        print("~")

# } Driver Code Ends