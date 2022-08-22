struct ListNode* middleNode(struct ListNode* head){
    if(head == NULL){
        return head;
    }
    int result;
    int count=0;
    struct ListNode *ptr = head;
    struct ListNode *temp;
    while (ptr != NULL){
        count++;
        ptr=ptr->next;
    }
    
    // printf("%d",count);
    if(count==1){
        return head;
    }
    
    for(int i=0; i<(count/2)-1; i++){
        head=head->next;
    }
    temp=head->next;
    return temp;
    
}
