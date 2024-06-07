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

# Solution
def reverseList(head):
    prev, curr = None, head
    
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
    return prev

if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    head = create_linked_list(values)

    # Reverse the linked list
    reversed_head = reverseList(head)

    # Print the reversed linked list
    while reversed_head:
        print(reversed_head.val, end=" ")
        reversed_head = reversed_head.next
