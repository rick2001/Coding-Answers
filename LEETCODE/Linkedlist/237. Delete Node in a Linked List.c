// code is avilable in both c and java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        node.val=node.next.val;
        node.next=node.next.next;
    }
}




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
