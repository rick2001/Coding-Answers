/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
//     optimal solution
//     T.C-> O(N)
//     S.C-> O(1)
    
    struct ListNode* dummyhead = (struct ListNode *) malloc(sizeof(struct ListNode));
    dummyhead->next=head;
    struct ListNode *slow=dummyhead;
    struct ListNode *fast=dummyhead;
    
    for(int i=1; i<=n; i++){
        fast=fast->next;
    }
    
    while(fast->next!=NULL){
        slow=slow->next;
        fast=fast->next;
    }
    slow->next = slow->next->next;
    return dummyhead->next;
    
    
    
    
//  bruteforce
//     struct ListNode* ptr=head;
//     struct ListNode* newhead=head;
//     struct ListNode* temp;
//     if (head==NULL){
//         return head;
//     }
//     int count=0;
//     while (ptr!=NULL){
//         count+=1;
//         ptr=ptr->next;
//     }
//     // printf("%d",count);
//     for(int i=0; i<count-n-1; i++){
//         head=head->next;
//     }
    
//     temp=head->next->next;
//     free(head->next);
//     head->next=temp;
//     return newhead;
    
    
    
    
    
    // return head;
}
