# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = l1
        str1 = ""
        while pointer1:
            str1 += f"{pointer1.val}"
            pointer1 = pointer1.next
        str1 = str1[::-1]

        pointer2 = l2
        str2 = ""
        while pointer2:
            str2 += f"{pointer2.val}"
            pointer2 = pointer2.next
        
        str2 = str2[::-1]

        total = str(int(str1) + int(str2))[::-1]

        newNode = ListNode(0)
        test = newNode
        for i in total:
            test.next = ListNode(i)
            test = test.next
        return newNode.next