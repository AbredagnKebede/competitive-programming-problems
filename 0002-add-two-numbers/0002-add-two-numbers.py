class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1new = []
        l2new = []
        root1 = l1
        root2 = l2
        while root1:
            l1new.append(root1.val)
            root1 = root1.next
        while root2:
            l2new.append(root2.val)
            root2 = root2.next
        l1new = l1new[::-1] 
        l2new = l2new[::-1] 
        s1 = int("".join(map(str, l1new)))   
        s2 = int("".join(map(str, l2new)))
        ans = map(int, str(s1+s2)[::-1])
        
        head =  ListNode(ans[0])
        temp = head
        for i in range(1, len(ans)):
            new_node = ListNode(ans[i])
            head.next = new_node
            head = head.next
        return temp
        