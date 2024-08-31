class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Adding a tail pointer for O(1) append operations

    def append(self, data: int):
        new_node = Node(data)
        if self.head is None:  # If the list is empty, head and tail are the new node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Link the last node to the new node
            self.tail = new_node       # Update the tail to the new node

    def find_max(self) -> int:
        if self.head is None:
            raise ValueError("List is empty")

        max_value = self.head.data
        current = self.head.next
        
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        
        return max_value

# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    print(ll.find_max())  # Output: 4
