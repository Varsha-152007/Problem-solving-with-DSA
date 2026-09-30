# Problem: Sort List
# Problem Link: https://leetcode.com/problems/sort-list/description/?envType=problem-list-v2&envId=sorting
# Date: 30th Sept 2026
# Time taken to solve: 35 min

#solution
<
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        values = []
        curr = head

        while curr:
            values.append(curr.val)
            curr = curr.next

        values = sorted(values)

        curr = head
        for value in values:
            curr.val = value
            curr = curr.next

        return head
        >
#Notes
#Converted the linked-list values into an array, sort the array, and copy the sorted values back into the linked list.
