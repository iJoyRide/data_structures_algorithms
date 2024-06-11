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
    """Iterative approach to reverse a linked list."""
    
    # Initialize pointers
    prev = None
    temp = head
    
    # Check if the list is empty or has only one element
    if head == None or head.next == None:
        return temp
    
    # Iterate through the list and reverse the pointers
    while temp:
        front = temp.next  # Store the next node temporarily
        temp.next = prev   # Reverse the pointer
        prev = temp        # Move prev pointer forward
        temp = front       # Move temp pointer forward
    
    return prev  # Return the new head of the reversed list

# Time complexity: O(N)
# Space complexity: O(1)

def reverseListRec(head):
    """Recursive approach to reverse a linked list."""
    
    # Recursive function to reverse the list
    def reverse(temp, prev):
        # Base case: if the current node is None, return the previous node
        if temp is None:
            return prev
        else:
            front = temp.next     # Store the next node temporarily
            temp.next = prev     # Reverse the pointer
            return reverse(front, temp)  # Recur with updated pointers

    # Start the recursion with the head of the original list and None as the previous node
    return reverse(head, None)

# Time complexity: O(N)
# Space complexity: O(N) due to recursion stack


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