class Solution:
    def oddEvenList(self, head: listNode) -> listNode:
        odd = head
        even_head = even = head.next
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        odd.next = even_head
        return head

