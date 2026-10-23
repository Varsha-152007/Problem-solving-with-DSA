# Problem: Insertion Sort List
# Problem Link: https://leetcode.com/problems/insertion-sort-list/description/?envType=problem-list-v2&envId=sorting
# Date: 23rd Oct 2026
# Time taken to solve: 35 mins

#solution
<
class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next

        arr.sort()

        curr = head
        for val in arr:
            curr.val = val
            curr = curr.next

        return head
>

#Note
#Store linked-list values in an array, sort them using sort(), and update the original nodes with the sorted values.
