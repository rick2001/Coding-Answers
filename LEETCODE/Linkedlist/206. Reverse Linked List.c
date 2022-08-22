/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){
    struct ListNode* newhead = NULL;
    struct ListNode* nextnode;
    if(head == NULL){
        return head;
    }
    else{
        while(head != NULL){
            nextnode=head->next;
            head->next = newhead;
            newhead = head;
            head = nextnode;
            // nex= nex->next;      
        }
        return newhead;
    }

}
