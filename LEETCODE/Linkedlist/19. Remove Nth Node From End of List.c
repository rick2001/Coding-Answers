// In both python and c language are written this code
// In Python Language

class Solution(object):
    def removeNthFromEnd(self, head, n):
        #Most Optimized Approach
        dummyHead = ListNode(0)
        dummyHead.next = head
        slow=dummyHead
        fast=dummyHead
        
        for i in range(1, n+1):
            fast=fast.next
        
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummyHead.next
        
         
        #BruteForce Approach
#         dummyHead1 = head
#         dummyHead2 = head
#         count=0
#         while dummyHead1!=None:   #Find the length
#             count+=1
#             dummyHead1=dummyHead1.next
#         count = count - n
#         print(count)
#         if count == 0: #it means from last head node is instructed to be deleted
#             return head.next
#         else:
#             for i in range(count-1):
#                 dummyHead2 = dummyHead2.next
#             dummyHead2.next = dummyHead2.next.next
#         return head

















// In c Language
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
