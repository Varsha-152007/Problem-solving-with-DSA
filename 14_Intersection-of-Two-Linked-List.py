# Problem: Intersection of Two Linked List
# Problem Link: https://leetcode.com/problems/intersection-of-two-linked-lists/description/?envType=problem-list-v2&envId=hash-table
# Date: 1st Sept 2026 
# Time taken to solve: 20 mins

#solution
<
lass Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a
      >

#Notes:
#Used two pointers approach, one starting at each linked list.
