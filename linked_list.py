class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self) -> None:
        self.head = None
    
    def append(self,data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            
        else:
            '''
               Suppose you have a linked list with two nodes: 1 -> 2 -> None. 
               You want to append a new node with the 
               value 3 to the end of this list.

                1. current_node = self.head: Initialize a variable current_node 
                to the head of the linked list, which is the node with the value 1.

                2. while current_node.next_node is not None:: This loop iterates 
                through the linked list until it finds the last node. In this example, 
                it checks if the next_node of the current node is not None. If it is 
                not None, it means there's another node, so we update current_node to
                be the next node and continue the loop.
                
                In the example:
                -->First iteration: current_node is the node with value 1. Its 
                next_node is the node with value 2, so we continue to the next iteration.
                -->Second iteration: current_node is the node with value 2. 
                Its next_node is None, so we exit the loop.
                
                3. current_node.next_node = new_node: After the loop, 
                current_node is the last node in the linked list (the node with value 2).
                We set the next_node of this last node to the new node (new_node with value 3).
                Now, the linked list becomes 1 -> 2 -> 3 -> None.
            '''
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = newNode
        
    def display(self):
        currentNode = self.head
        while currentNode.next is not None:
            print(currentNode.data, end=' --> ')
            currentNode = currentNode.next
        print(None)


if __name__=='__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(4)
    ll.append(2)
    ll.display()