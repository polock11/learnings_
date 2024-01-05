class Node():
    def __init__(self, val=None, next=None) -> None:
        self.val=val
        self.next=next

class LinkedList():
    def __init__(self) -> None:
        self.head=None
    
    def append(self, val):
        newNode = Node(val)
        
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while lastNode.next is not None:
                lastNode = lastNode.next
            lastNode.next = newNode
    
    def remove_first(self):
        if self.head ==None : return

        new_head = self.head.next
        self.head = new_head
    
    def remove_last(self):
        currentNode  = self.head
        while currentNode.next.next is not None:
            currentNode = currentNode.next
        currentNode.next = None
    
    def show_with_idx(self):
        lastNode = self.head
        idx = 0
        while lastNode is not None:
            print(f'val: {lastNode.val} idx: {idx}', end= ' --> ')
            lastNode = lastNode.next
            idx = idx+1
        print(None)

    def insert_at(self, val, idx):
 
        if idx > self.length():
            print('Wrong index')
            return

        currentNode = self.head
        newNode = Node(val)
        counter = 0

        if idx == 1:
            rest_element = currentNode.next.next
            currentNode.next = newNode
            newNode.next = rest_element
        else:    
            while currentNode.next is not None:
                currentNode = currentNode.next
                counter = counter + 1
                if counter == idx-1:
                    rest = currentNode.next
                    currentNode.next = newNode
                    newNode.next = rest
    
    def length(self):
        currentNode = self.head
        counter = 0
        while currentNode.next:
            currentNode = currentNode.next
            counter += 1
        return counter+1 

    def show(self):
        lastNode = self.head
        while lastNode is not None:
            #print(f'||val:{lastNode.val} next: {lastNode.next} ||', end=' --> ')
            print(lastNode.val, end=' --> ')
            lastNode = lastNode.next
            
        print('None')

if __name__=='__main__':
    ll = LinkedList()

    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.show()
    # print(ll.length())
    # ll.remove_first()
    # ll.show()
    # print('---------------')
    # ll.remove_first()
    # ll.show()
    # ll.remove_last()
    # ll.show()
    # ll.insert_at(44,2)
    # ll.show()
    ll.insert_at(55,4)
    ll.show()
