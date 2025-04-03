# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def deleteNode(head, x):
    
    if not head:
        return None
    if x==1:
        head=head.next
        return head
    temp=head
    while temp and x>0:
        x-=1
        if x==1:
            break
        temp=temp.next
    temp.next=temp.next.next
    return head
        


#{ 
 # Driver Code Starts
# Node Class
class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.last = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.last = self.head
        else:
            self.last.next = new_node
            self.last = new_node


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print('')


# Driver Program
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        list1 = LinkedList()
        values = list(map(int, input().strip().split()))
        for value in values:
            list1.insert(value)
        k = int(input())
        new_head = deleteNode(list1.head, k)
        print_list(new_head)
        print("~")
# } Driver Code Ends