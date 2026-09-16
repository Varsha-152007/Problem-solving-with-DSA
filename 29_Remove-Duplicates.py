# Problem: Remove Duplicates from Sorted List
# Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Date: 16th Sept 2026
# Time taken to solve: 25 min

#solution
<
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
      >

