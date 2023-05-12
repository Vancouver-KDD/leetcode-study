class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        new_head = head

        while new_head.next:
            temp = new_head.next
            new_head.next = temp.next
            temp.next = head
            head = temp

        return head


def main():
    s = Solution()
    five = ListNode(val=5)
    four = ListNode(val=4, next=five)
    three = ListNode(val=3, next=four)
    two = ListNode(val=2, next=three)
    one = ListNode(val=1, next=two)
    result = s.reverseList(one)


if __name__ == '__main__':
    main()
