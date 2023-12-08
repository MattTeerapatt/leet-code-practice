from typing import Optional


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None 
        current = head

        while current:
            next_node = current.next
            current.next = new_list
            new_list = current 
            current = next_node 

        return new_list

# Create a linked list from the input
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head2 = ListNode(1, ListNode(2))

# Create a solution instance
solution = Solution()

# Reverse the linked list
result = solution.reverseList(head)
result2 = solution.reverseList(head2)


while result:
    print(result.value, end=" ")
    result = result.next
