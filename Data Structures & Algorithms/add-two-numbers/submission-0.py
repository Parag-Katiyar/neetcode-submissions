# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        x = l1
        y = l2
        carry = 0 
        flag = 0 

        while x or y or carry: 

            if x is None and y: 
                digit = (carry + y.val)%10
                carry = (carry + y.val)//10

                y.val = digit
                
                flag_node = y
                y = y.next
                flag = 1 

            
            elif y is None and x: 
                digit = (carry + x.val)%10
                carry = (carry + x.val)//10

                x.val = digit

                flag_node = x
                x = x.next
                flag = 2

            else: 
                digit = (carry + x.val + y.val)%10
                carry = (carry + x.val + y.val)//10

                flag_x = x

                x.val = digit
                y.val = digit 

                x = x.next
                y = y.next 

                 
            
            if y is None and x is None and carry != 0:

                new_node = ListNode(carry)
                if flag == 1: 

                    flag_node.next = new_node
                    new_node.next = None
                    return l2
                
                if flag == 2:
                    flag_node.next = new_node
                    new_node.next = None
                    return l1

                if flag == 0: 
                    
                    flag_x.next = new_node
                    new_node.next = None
                    return l1


        if flag == 1: 
            return l2 
        if flag == 2: 
            return l1 
        if flag ==0: 
            return l1




            








