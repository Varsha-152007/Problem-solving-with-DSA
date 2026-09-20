# Problem: Merge Two Sorted Lists
# Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/description/
# Date: 20th Sept 2026
# Time taken to solve: 40 min

#solution
<
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
      >
#Notes
#Compared the current nodes of both sorted lists, link the smaller node, and recursively merge the remaining nodes.



