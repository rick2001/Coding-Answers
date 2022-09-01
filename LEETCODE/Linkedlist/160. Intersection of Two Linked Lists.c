/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
//     Bruteforce or Naive solution
//     T.C->O(N^2)
//     S.C->O(1)
    // while(headA!=NULL){
    //     struct ListNode *temp=headB;
    //     while(temp!=NULL){
    //         if (headA==temp)return headA;
    //         temp=temp->next;
    //     }
    //     headA=headA->next;
    // }
    // return NULL;
    
    
//     optimal-1
    // T.C->O(N)
    // S.C->O(1)
    
//     struct ListNode *a=headA;
//     struct ListNode *b=headB;
//     int count1=0; //considering count1 for headA
//     int count2=0; //considering count1 for headB
    
//     while(a!=NULL){
//         count1+=1;
//         a=a->next;
//     }
//     while(b!=NULL){
//         count2+=1;
//         b=b->next;
//     }
//     int difference;
//     if(count1>count2){ 
//         difference=count1-count2;
//         for(int i=0;i<difference;i++){
//             headA=headA->next;
//         }
//         while(headA!=NULL && headB!=NULL){
//             if(headA==headB){
//                 return headA;
//             }
//             headA=headA->next;
//             headB=headB->next;
//         }
        
//     }
//     else{
//         difference=count2-count1;
//         for(int i=0;i<difference;i++){
//             headB=headB->next;
//         }
//         while(headA!=NULL && headB!=NULL){
//             if(headB==headA){
//                 return headB;
//             }
//             headA=headA->next;
//             headB=headB->next;
//         }
    
//    }
//    return NULL;
    
    
    
    
    // best approach (optimal-2)
    if(headA==NULL || headB==NULL){
        return NULL;
    }
    
    struct ListNode *a=headA;
    struct ListNode *b=headB;
    
    while(a!=b){
        if(a==NULL)a=headB;
        else a=a->next;
        
        if(b==NULL)b=headA;
        else b=b->next;       
    }
    return a;    //we can return a and b both. because both are same as it is intersecting in same node. so whatever adress we return it is same
    
}
