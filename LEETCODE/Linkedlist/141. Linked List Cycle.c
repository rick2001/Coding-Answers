/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

#c language
bool hasCycle(struct ListNode *head) {
//     Most optimized
    if(head==NULL || head->next==NULL){
        return 0;
    }
    
    struct ListNode *fast=head;
    struct ListNode *slow=head;
    
    while (fast->next!=NULL && fast->next->next!=NULL){
        fast=fast->next->next;
        slow=slow->next;
        
        if(fast==slow){
            return 1;
        }
    }
    return 0; 
    
}


#python

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    
    def hasCycle(self, head):
        #bruteforce 
        # T.C-> O(N)
        # S.C-> O(N)
        
        # hashi=[]
        # # ListNode ptr = head
        # while head!=None:
        #     if head in hashi:
        #         return True
        #     else:
        #         hashi.append(head)
        #         head=head.next
        # return False
        
        
        # T.C-> O(N)
        # S.C-> O(1)
        # Most optimized
        if head ==None or head.next == None:
            return False
        
        slow=head
        fast=head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                return True
        return False
    
    
        
        
        
        
        
        """
        :type head: ListNode
        :rtype: bool
        """
        
