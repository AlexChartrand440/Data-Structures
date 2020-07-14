"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):

        newNode = ListNode(value);

        if self.head is None: # List is empty, assign to both
            self.head = newNode;
            self.tail = newNode;
        else: # Shift the list and add the new head
            self.head.prev = newNode;
            newNode.next = self.head;
            self.head = newNode;

        self.length += 1;
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):

        if self.head is None: # List is empty
            return None;
        elif self.head is self.tail: # If the list only has one entry, head will equal the tail
            value = self.head.value;

            self.length -= 1;
            self.head = None;
            self.tail = None;

            return value;
        else: # Remove the existing head and shift the list

            self.length -= 1;

            value = self.head.value;

            self.head = self.head.next;
            self.head.prev = None;

            return value;
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):

        newNode = ListNode(value);
        self.length += 1;

        if self.head is None: # List is empty, assign value to both head and tail
            self.head = newNode;
            self.tail = newNode;
        else: # Tail exists, add to list and update the old tail
            newNode.prev = self.tail;
            self.tail.next = newNode;
            self.tail = newNode;
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None: # List is empty
            return None;
        elif self.length <= 1: # List only has one value
            value = self.tail.value;

            self.head = None;
            self.tail = None;
            self.length -= 1;
            
            return value;
        else: # List has more than a single value
            value = self.tail.value;

            self.tail = self.tail.prev;
            self.length -= 1;

            return value;

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node.next is None and node.prev is None: # Only item in list
            pass; # Assumed to already be at the front
        elif node.next is None: # Tail
            oldTail = self.tail;
            oldHead = self.head;

            newTail = oldTail.prev;
            newTail.next = None;

            self.tail = newTail;

            oldHead.prev = oldTail;
            oldTail.next = oldHead;

            self.head = oldTail;
        elif node.prev is None: # Head
            pass; # Assumed to already be at the front
        else: # Between items
            fNode = node.next; # Node ahead of current in list
            bNode = node.prev; # Node behind of current in list

            fNode.prev = bNode; # Front node prev is reassigned to back node
            bNode.next = fNode; # Back node next is reassigned to front node

            oldHead = self.head;

            node.prev = None;
            node.next = oldHead;

            oldHead.prev = node;
            self.head = node;
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node.next is None and node.prev is None: # Only item in list
            pass; # Assumed to already be at the end
        elif node.next is None: # Tail
            pass; # Assumed to already be at the end
        elif node.prev is None: # Head
            oldHead = self.head;
            oldHead.prev = self.tail;

            newHead = oldHead.next;
            newHead.prev = None;

            oldTail = self.tail;
            oldTail.next = oldHead;

            self.head = newHead;
            self.tail = oldHead;
        else: # Between items
            fNode = node.next; # Node ahead of current in list
            bNode = node.prev; # Node behind of current in list

            fNode.prev = bNode; # Front node prev is reassigned to back node
            bNode.next = fNode; # Back node next is reassigned to front node

            oldTail = self.tail;

            node.next = None;
            node.prev = oldTail;

            oldTail.next = node;

            self.tail = node;

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        
        current = self.head;

        while current: # Stop the loop when the current node is None
            if current is node:
                if current.next is None and current.prev is None: # Only item in list
                    self.head = None; # Only item in the list can be assumed
                    self.tail = None; # to be both head and tail

                    self.length -= 1; # If any was found, remove 1 from the total length of the list
                elif current.next is None: # Tail
                    self.remove_from_tail();
                elif current.prev is None: # Head
                    self.remove_from_head();
                else: # Between items
                    fNode = current.next; # Node ahead of current in list
                    bNode = current.prev; # Node behind of current in list

                    fNode.prev = bNode; # Front node prev is reassigned to back node
                    bNode.next = fNode; # Back node next is reassigned to front node

                    self.length -= 1; # If any was found, remove 1 from the total length of the list

            current = current.next; # Next node in list

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None;

        max_value = self.head.value;

        current = self.head.next;

        while current: # Stop the loop when the current node is None
            if current.value > max_value:
                max_value = current.value;

            current = current.next;

        return max_value