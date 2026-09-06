# Problem: Palindrome Linked List
# Problem Link: https://leetcode.com/problems/palindrome-linked-list/description/?envType=problem-list-v2&envId=stack
# Date: 6th Sept 2026
# Time taken to solve: 50 mins

#solution
<
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True   
      >
#Notes
#Used slow/fast pointers approach
