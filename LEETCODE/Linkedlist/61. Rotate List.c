/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* rotateRight(struct ListNode* head, int k){
//     Most optimized Approach
//     T.C -> O(N)
//     S.C -> O(1)
    
//     Edge cases
    if (head==NULL || head->next==NULL || k==0){
        return head;
    }
    
    int len=1;
    struct ListNode *ptr = head;
    while(ptr->next!=NULL){  //counting the length of the linkedlist
        
        len+=1;
        ptr=ptr->next;
    }
    
    ptr->next=head; //making it circular
    k=k % len;
    k=len-k;
    
    while(k>0){
        ptr=ptr->next;
        k--;
    }
    head=ptr->next;
    ptr->next=NULL;
    
    return head;
    
    
    
    
    
//     BruteForce Approach
//     but here we will get Time Limit Exceeded for this input. Mentioned below
//     [1,2,3]
//     2000000000
    
//     if (head==NULL){
//         return NULL;
//     }
    
//     if(head->next==NULL){
//         return head;
//     }
    
    
//     int j=0;
//     while(j<k){
//         struct ListNode* ptr=head;
//         struct ListNode* dum=head;
//         while(ptr->next->next!=NULL){
//             ptr=ptr->next;
//         }
//         struct ListNode *temp = (struct ListNode *)malloc(sizeof(struct ListNode));
//         temp->val = ptr->next->val;
//         free(ptr->next);
//         ptr->next=NULL;
//         temp->next=dum;
//         head=temp;
//         j++;
//     }
//     return head;
    

}
