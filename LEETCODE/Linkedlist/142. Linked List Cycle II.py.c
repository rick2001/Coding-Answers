
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// Using C (Most Optimized Approach)
struct ListNode *detectCycle(struct ListNode *head) {
    
//     Most Optimized
    // T.C-> O(N)
//     S.C-> O(1)
    
    if(head==NULL || head->next==NULL){
        return NULL;
    }
    
    struct ListNode *fast=head;
    struct ListNode *slow=head;
    struct ListNode *entry=head;
    
    while (fast->next!=NULL && fast->next->next!=NULL){
        fast=fast->next->next;
        slow=slow->next;
        if(fast==slow){
            
            while(slow!=entry){
                slow=slow->next;
                entry=entry->next;
            }
            return slow;    //i can return either slow or slow because both are same
        }
    }
    return NULL;
}



#using python (BruteForce)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
#         bruteforce approach using hashtable
        # T.C-> O(N)
#         S.C-> O(1)
        
        if head==None or head.next==None:
            return None
        
        
        hashtable=[]
        count=0
        while head!=None:
            if head in hashtable:
                return head
            else:
                hashtable.append(head)
                head=head.next
        return None
        
        
        
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
