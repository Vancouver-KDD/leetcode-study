class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        result = None

        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            result = ListNode(val=list2.val)
            if list1.val < list2.val:
                result = ListNode(val=list1.val)
                list1 = list1.next
            list2 = list2.next

        head = result

        while list1 or list2:
            if list1 is None:
                result.next = list2
                return head
            if list2 is None:
                result.next = list1
                return head
            if list1.val <= list2.val:
                result.next = ListNode(val=list1.val)
                result = result.next
                list1 = list1.next
            elif list2.val < list1.val:
                result.next = ListNode(val=list2.val)
                result = result.next
                list2 = list2.next
        return head


def main():
    s = Solution()
    four = ListNode(val=4)
    two = ListNode(val=2, next=four)
    one = ListNode(val=1, next=two)

    four2 = ListNode(val=4)
    three = ListNode(val=3, next=four2)
    one2 = ListNode(val=1, next=three)
    result = s.mergeTwoLists(one, one2)
    while result.next:
        print(result.val)
        result = result.next

if __name__ == '__main__':
    main()