# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        dummy = head
        while dummy: 
            length +=1
            dummy = dummy.next
        if length == 1:
            return None
        index = length - n
        dummy = pre = head
        cnt = 0
        if index == 0:
            head = head.next
        while dummy:
            if cnt == index-1:
                pre = dummy
            if cnt == index:
                pre.next = dummy.next
                break 
            dummy = dummy.next
            cnt +=1
        return head
    


