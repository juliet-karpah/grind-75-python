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