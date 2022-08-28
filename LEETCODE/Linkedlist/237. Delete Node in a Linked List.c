/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void deleteNode(struct ListNode* node) {
    // struct ListNode* temp;
    // at first replacing the node val with next node val
//      then simply pointing the node next part with the next node next part tahts it!!!!
    node->val=node->next->val;
    node->next=node->next->next;
}
