/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *reverselist(struct ListNode* head){    //defining the reverse list function by ourself
    struct ListNode* prev=NULL;
    struct ListNode* nextnode;
    while(head!=NULL){
        nextnode = head->next;
        head->next=prev;
        prev=head;
        head=nextnode;
    }
    return prev;
}

// Most optimized approach

// T.C-> O(N/2)
// S.C-> O(1)
bool isPalindrome(struct ListNode* head){
    if(head==NULL || head->next==NULL){
        return 1;
    }
    struct ListNode* slow=head;
    struct ListNode* fast=head;
    
    while(fast->next!=NULL && fast->next->next!=NULL){
        slow=slow->next;
        fast=fast->next->next;
    }
    
    slow->next=reverselist(slow->next);
    slow=slow->next;
    
    while(slow!=NULL){
        if(head->val!=slow->val){
            return 0;
        }
        head=head->next;
        slow=slow->next;
    }
    return 1;
}

