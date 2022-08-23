/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* middleNode(struct ListNode* head){
    
//     T.C-> O(N/2)
//     S.C-> O(1)
//     Optimal solution
//     we will use slow and fast tortoise method
//     slow pointer will move by one step and the fast pointer will move by 2 step;
    
    if(head == NULL){
        return head;
    }
    
    struct ListNode *slow = head;
    struct ListNode *fast = head;
    
    while (fast!=NULL && fast->next!=NULL){
        slow=slow->next;
        fast=fast->next->next;
    }
    return slow;
    
    
//     Bruteforce solution
//     T.C-> O(N)+O(N/2)
//     S.C-> O(1)
//     if(head == NULL){
//         return head;
//     }
    
//     int count=0;
//     struct ListNode *ptr = head;
//     struct ListNode *temp;
//     while (ptr != NULL){
//         count++;
//         ptr=ptr->next;
//     }
    
//     // printf("%d",count);
//     if(count==1){
//         return head;
//     }
    
//     for(int i=0; i<(count/2); i++){
//         head=head->next;
//     }
//     // temp=head;
//     return head;
   
