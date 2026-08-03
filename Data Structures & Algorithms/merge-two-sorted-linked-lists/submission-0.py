# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def pt(x1, x2, point):
    if x1 == None: 
        point.next = x2
        return 
    if x2 == None: 
        point.next = x1 
        return 

    if x1.val < x2.val: 
        point.next = x1 
        point = x1 
        x1 = x1.next 
        return pt(x1, x2, point)

    if x1.val > x2.val:
        point.next = x2 
        point = x2 
        x2 = x2.next 
        return pt(x1, x2, point)

    if x1.val == x2.val: 
        # Only attach x1 this round. Let the next recursive pass naturally 
        # see that x2 matches or fits next. This keeps pointers clean!
        point.next = x1 
        point = x1 
        x1 = x1.next 
        return pt(x1, x2, point)



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None: 
            return list2 
        if list2 == None: 
            return list1 
        
        if list1.val <= list2.val:
            head = list1
            pt(list1.next, list2, head)
            return head
        else:
            head = list2
            pt(list1, list2.next, head)
            return head
        









