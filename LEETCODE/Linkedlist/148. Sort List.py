# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        #this is the brute force approach
        lst=[]
        tempHead1=head
        tempHead2=head
        while tempHead1!=None:  #add in list
            lst.append(tempHead1.val)
            tempHead1=tempHead1.next
        lst.sort()  # sort the list
        index=0
        while tempHead2!=None:
            tempHead2.val=lst[index]
            index+=1
            tempHead2=tempHead2.next
        return head
            
        
