# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# list1 = [1,2,4], list2 = [1,3,4] => [1,1,2,3,4,4]
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next