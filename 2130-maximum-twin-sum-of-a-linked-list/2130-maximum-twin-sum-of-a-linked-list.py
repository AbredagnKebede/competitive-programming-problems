class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        maxsum = 0
        while slow:
            maxsum = max(maxsum, stack.pop() + slow.val)
            slow = slow.next

        return maxsum