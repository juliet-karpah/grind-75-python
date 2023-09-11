"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(self, list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    first_node = curr = ListNode()
    while list1 and list2:
        if list1.val > list2.val:
            first_node.next = list2
            list2, first_node = list2.next, list2
        else:
            first_node.next = list1
            list1, first_node = list1.next, list1
    if list1:
        first_node.next = list1
    elif list2:
        first_node.next = list2
    return curr.next