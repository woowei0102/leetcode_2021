/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
/* method 1
    bool hasCycle(ListNode *head) {
        if (head == NULL) return false;
        ListNode *fast = head;
        ListNode *slow = head;
        while (fast->next != NULL && fast->next->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) return true;
        }
        return false;
        
    }
*/
    bool hasCycle(ListNode *head) {
        try {
            ListNode *fast = head->next;
            ListNode *slow = head;
            while (fast != slow) {
                fast = fast->next->next;
                slow = slow->next;
            }
            return true;
        } catch (exception &e){
            return false;
        }
        
    }
};