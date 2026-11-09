# Problem: Remove Nth Node From End of List
# Problem Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Date: 9th Nov 2026
# Time taken to solve: 35 mins

#solution
<
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        if count == n:
            return head.next

        curr = head

        for i in range(count - n - 1):
            curr = curr.next

        curr.next = curr.next.next

        return head
>
#Notes
#Count the nodes, move to the node before the target, and update its next pointer to skip the node to be deleted.
