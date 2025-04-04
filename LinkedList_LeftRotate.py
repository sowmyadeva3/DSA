class Solution:
    
    # Function to rotate a linked list to the left by k nodes.
    def rotate(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Step 1: Count total nodes
        temp = head
        count = 1
        while temp.next:
            temp = temp.next
            count += 1

        # Step 2: Normalize k
        k = k % count
        if k == 0:
            return head

        # Step 3: Traverse to the kth node
        temp1 = head
        for _ in range(k - 1):
            temp1 = temp1.next

        # Step 4: Reconnect nodes
        newHead = temp1.next
        temp1.next = None
        temp.next = head

        return newHead
