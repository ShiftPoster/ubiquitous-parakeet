from .common import ListNode


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        if l1 is None and l2 is None:
            start = None
        else:
            carry = False
            start = ListNode()
            sum_ll = start
            curr_1 = ListNode() if l1 is None else l1
            curr_2 = ListNode() if l2 is None else l2

            while True:
                sum_ll.val = curr_1.val
                sum_ll.val += curr_2.val
                sum_ll.val += 1 if carry else 0
                carry = sum_ll.val >= 10
                sum_ll.val -= 10 if carry else 0

                if curr_1.next is None and curr_2.next is None:
                    break

                curr_1 = ListNode() if curr_1.next is None else curr_1.next
                curr_2 = ListNode() if curr_2.next is None else curr_2.next

                new = ListNode()
                sum_ll.next = new
                sum_ll = new

            if carry is True:
                sum_ll.next = ListNode(1)

        return start


def run(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    return Solution().addTwoNumbers(l1, l2)
