

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        #  Loop through all nodes and count one for each
        total = self.head #number of nodes
        count = 0 #initialize the count
        while(total): #loop through all nodes
            count += 1
            total = total.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list."""

        """TODO: Running time: O(???) Why and under what conditions?"""

        #  Create new node to hold given item
        new_node = Node(item)
        #  Append node after tail, if it exists
        if self.tail == None and self.head == None: #if the list is empty
            self.head = new_node
            self.tail = new_node
        else: #already has something in list
            #if already a node as the tail
            #we need to put our new node after the tail
            self.tail.next = new_node
            #reset the tail to the new_node
            self.tail = new_node


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        #  Create new node to hold given item
        new_node = Node(item)
        #  Prepend node before head, if it exists
        if self.tail == None and self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        #quality is a function being passed
        #  Loop through all nodes to find item where quality(item) is True
        current = self.head
        while current != None: #making sure there is a value
            print("current node", current.data)
            print(quality(current.data))
            if quality(current.data) == True: #looping to find one that matches
                return current.data
            else: #found
                current = current.next  #move head to the next
        return None #not found



        #  Check if node's data satisfies given quality function

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        if self.is_empty():
            raise ValueError('Item not found: {}'.format(item))
            return
        currentNode = self.head
        if currentNode.data == item: #if head has the item
            self.head = currentNode.next #if head has next... assign next as new head
            if currentNode.next == None: #head is the last item... set self.tail to none
                self.tail = None
            return
        prev = None
        while currentNode != None: #loop until we reach tail
            print("Current node =", currentNode)
            if currentNode.data == item: #if node's data is the item... found!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                if currentNode.next == None: #if currentNode is the tail because it has no next...
                    self.tail = prev #prev node will now be the new tail
                prev.next = currentNode.next #DELETE currentNode by removing prev's next (reference) to currentNode's next
                return
            # TODO: Update previous node to skip around node with matching data
            prev = currentNode #if currentNode's data is not item, 
            currentNode = currentNode.next #keep going til it reach the tail
            print("Current.next = ", currentNode)
        # TODO: Otherwise raise error to tell user that delete has failed
        raise ValueError('Item not found: {}'.format(item))


        #  Update previous node to skip around node with matching data
        # Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
    def print_ll(self):
        current = self.head
        while current != None:
            print("print", current.data)
            current = current.next

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()