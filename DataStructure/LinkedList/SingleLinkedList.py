# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# list1 = [1,2,4], list2 = [1,3,4] => [1,1,2,3,4,4]
class Solution:
    def mergeTwoLists(self, list1, list2): # both ListNodes
        head = ListNode()
        current = head

        while list1 != None and list2 != None: # until one of them are empty
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next # also current moves

        if list1 != None: # if sth left
            current.next = list1
        if list2 != None:
            current.next = list2

        return head.next
    
    