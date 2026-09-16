# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        a = []
        m = head

        while m:
            if m.val not in a:
                a.append(m.val)
            m = m.next

        dummy = ListNode()
        curr = dummy

        for x in a:
            curr.next = ListNode(x)
            curr = curr.next

        return dummy.next
    