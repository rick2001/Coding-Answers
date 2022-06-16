/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *dummynode = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *temp = dummynode;
    int carry = 0;
    while (l1 != NULL || l2 != NULL || carry){
        int sum = 0;
        
        if(l1 != NULL){
            sum+=l1->val;
            l1 = l1->next;
        }
        
        if(l2 != NULL){
            sum+=l2->val;
            l2 = l2->next;
        }
        
        sum+=carry;
        carry = sum / 10;
        temp->val = (sum%10);
        if (l1!= NULL || l2 != NULL || carry){
            struct ListNode *node = (struct ListNode *)malloc(sizeof(struct ListNode));
            temp->next = node;
            temp= temp->next;
        }
            
    }
    temp->next = NULL;
    // temp = NULL;
    return dummynode;
    

}
