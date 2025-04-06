#1.Basic creating new list




# #User function Template for python3
'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self,head1, head2):
        temp1,temp2 = head1,head2
        temp=None
        while temp1 and temp2:
            if temp1.data<temp2.data:
                newNode = Node(temp1.data)
                temp1=temp1.next
            else:
                newNode=Node(temp2.data)
                temp2=temp2.next
            if not temp:
                temp=newNode
                head=temp
            else:
                temp.next=newNode
                temp=temp.next
                newNode.next=None
        while temp1:
            newNode = Node(temp1.data)
            temp.next=newNode
            temp=temp.next
            newNode.next=None
            temp1=temp1.next
        while temp2:
            newNode = Node(temp2.data)
            temp.next=newNode
            temp=temp.next
            newNode.next=None
            temp2=temp2.next
            
        return head
#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=' ')
        temp = temp.next
    print()
    print("~")


def insert_sorted(head, data):
    new_node = Node(data)
    if not head or head.data >= data:
        new_node.next = head
        return new_node

    current = head
    while current.next and current.next.data < data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        input1 = list(map(int, input().split()))
        input2 = list(map(int, input().split()))

        head1 = None
        for item in input1:
            head1 = insert_sorted(head1, item)

        head2 = None
        for item in input2:
            head2 = insert_sorted(head2, item)

        obj = Solution()
        merged_head = obj.sortedMerge(head1, head2)
        print_list(merged_head)

# } Driver Code Ends

#****************************************************************************************************
#Optimized version in-place merge


#User function Template for python3
'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self,head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
            
        if head1.data<=head2.data:
            mergedHead= head1
            head1=head1.next
        else:
            mergedHead = head2
            head2=head2.next
            
        curr = mergedHead  
        
        while head1 and head2:
            if head1.data<=head2.data:
                curr.next=head1
                head1=head1.next
            else:
                curr.next=head2
                head2=head2.next
            curr=curr.next
        
        if head1:
            curr.next=head1
        if head2:
            curr.next=head2
        return mergedHead
#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=' ')
        temp = temp.next
    print()
    print("~")


def insert_sorted(head, data):
    new_node = Node(data)
    if not head or head.data >= data:
        new_node.next = head
        return new_node

    current = head
    while current.next and current.next.data < data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        input1 = list(map(int, input().split()))
        input2 = list(map(int, input().split()))

        head1 = None
        for item in input1:
            head1 = insert_sorted(head1, item)

        head2 = None
        for item in input2:
            head2 = insert_sorted(head2, item)

        obj = Solution()
        merged_head = obj.sortedMerge(head1, head2)
        print_list(merged_head)

# } Driver Code Ends