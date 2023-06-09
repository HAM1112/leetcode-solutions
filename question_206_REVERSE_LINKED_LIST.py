# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        list1 = []
        pointer = head
        while pointer is not None:
            list1.append(pointer.val)
            pointer = pointer.next
        
        list1 = list1[::-1]

        testNode = ListNode(0)
        test = testNode

        for i in list1:
            test.next = ListNode(i)
            test = test.next
        
        return testNode.next

        