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
    """Iterative"""

    prev = None
    temp = head
    
    if head == None or head.next == None:
        return temp
    while temp:
        
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    
    return prev

# Time = O(N)
# Space = O(1)

def reverseListRec(head):
    """Recursive"""

    # head is passed as cur, and None is passed as prev
    def reverse(temp, prev):
        if temp is None:
            return prev
        else:
            front = temp.next
            temp.next = prev
            return reverse(front, temp)

    return reverse(head, None)

# Time = O(N)
# Space = O(1)

if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    head = create_linked_list(values)

    # Reverse the linked list
    reversed_head_iter = reverseList(head)
    reversed_head_rec = reverseListRec(head)  # This will give incorrect result

    # Print the reversed linked list using iterative method
    print("Reversed list (Iterative): ", end="")
    while reversed_head_iter:
        print(reversed_head_iter.val, end=" ")
        reversed_head_iter = reversed_head_iter.next

    print()  # Print a newline for separation

    # Print the reversed linked list using recursive method
    print("Reversed list (Recursive): ", end="")
    reversed_head_rec = reverseListRec(create_linked_list(values))  # Create a new reversed list
    while reversed_head_rec:
        print(reversed_head_rec.val, end=" ")
        reversed_head_rec = reversed_head_rec.next