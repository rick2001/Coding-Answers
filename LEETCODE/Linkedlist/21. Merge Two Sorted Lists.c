/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// solution is present in Java and c both languages

//java
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if(list1==null && list2==null){
            return null;
        }
        if(list1!=null && list2==null){
            return list1;
        }
        if(list2!=null && list1==null){
            return list2;
        }
        
        ListNode ansNode=new ListNode(0);
        ListNode dummy=ansNode;
        
        
        while(list1!=null && list2!=null){
            if(list1.val <= list2.val){
                ansNode.next=list1;
                ansNode=ansNode.next;
                list1=list1.next;
            }
            else{
                ansNode.next=list2;
                ansNode=ansNode.next;
                list2=list2.next;
            }
        }
        
        if(list1!=null){
            ansNode.next=list1;
        }
        if(list2!=null){
            ansNode.next=list2;
        }
        
        return dummy.next;
        
    }
}

// C

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    
    
    
// Most Optimized Approach
//     T.C-> O(N)
//     S.C-> O(1)
    if(list1==NULL && list2==NULL){
        return NULL;
    }
     
    if(list1==NULL && list2!=NULL){
        return list2;
    }
    
    if(list1!=NULL && list2==NULL){
        return list1;
    }
    
    
    struct ListNode *temp = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode *newhead=temp;
    
    while (list1!=NULL && list2!=NULL){
        if (list1->val < list2->val){
            temp->next = list1;
            temp=temp->next;
            list1=list1->next;
        }
        else{
            temp->next = list2;
            temp=temp->next;
            list2=list2->next;
        }
    }
    if (list1 != NULL){
        temp->next = list1;
    }
    else{
        temp->next = list2;
    }
    
    return newhead->next;
    
}
