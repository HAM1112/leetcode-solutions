# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li = []
        pointer = head
        while pointer:
            li.append(pointer.val)
            pointer = pointer.next
        
        lenn = (len(li) +2)//2
        current = head
        counter = 1
        while current:
            if counter == lenn:
                head = current
            current = current.next
            counter +=1 
        return head
            