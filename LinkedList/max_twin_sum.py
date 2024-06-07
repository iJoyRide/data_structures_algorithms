class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    if not values:
        return None
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]

class Solution:
    @staticmethod
    def pairSum(head):
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
            
        return res
    
# Time complexity: O(N)
# Space complexity: O(1) 

if __name__ == "__main__":
    values = [5, 4, 2, 1]
    head = create_linked_list(values)
    result = Solution.pairSum(head)

    # Since you want to see the reversed linked list, you will need to define how to reverse it correctly here.
    # If you need help implementing the reverse list function or anything else, let me know!
    
    print("Maximum twin sum of linked list:", result)
