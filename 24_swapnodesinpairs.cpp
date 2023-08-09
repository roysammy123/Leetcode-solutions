class Solution {
public:
    ListNode* swapPairs(ListNode* head) 
    {
        ListNode *ptr, *ptr1, *ptr2, *temp;

        if ((head == NULL) || (head->next == NULL))
        {
            return head;
        }
        else
        {
            ptr = head;
            temp = ptr;
            ptr1 = ptr->next;
            ptr->next = ptr1->next;
            ptr1->next=temp;
            ptr2 = ptr;
            ptr = ptr->next;
            head = ptr1;

            while(ptr != NULL)
            {   
                if (ptr->next == NULL)
                    return head;
                else
                {
                    temp = ptr;
                    ptr1 = ptr->next;
                    ptr->next = ptr1->next;
                    ptr1->next=temp;
                    ptr2->next = ptr1;
                    ptr2 = ptr;
                    ptr = ptr->next;
                }
            }

            return head;
        }
    }
};
