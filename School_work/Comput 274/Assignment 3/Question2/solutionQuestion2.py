# Name: Antony Feng
# ccid: zfeng8
# studentId: 1802829
# operating system: windows 11
# python version: 3.12

# Starter Code from https://www.geeksforgeeks.org/python-linked-list/
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at begin of LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, data, index):
        if (index == 0):
            self.insertAtBegin(data)
            
        position = 0
        current_node = self.head
        while (current_node != None and position+1 != index):
            position = position+1
            current_node = current_node.next

        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    # Method to add a node at the end of LL
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    # Update node of a linked list at a given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

    # Print the size of linked list
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0

    # Print method for the linked list
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()
            
    # Removes all duplicate nodes from the linked list
    def remove_duplicates(self):
        # TODO: Your Implementation Here

        current_node = self.head

        if current_node is None or current_node.next is None: # return self.head if the linked list is None existent or the next
            return self.head

        while current_node != None: #while loop as long as current_node object is not empty
            next_node = current_node #set the next_node at first as a copy of the current node (head)

            while next_node.next != None: # while next_node is not empty

                if next_node.next.data == current_node.data: #if next_node.next value is the same as current node value point to the next next node

                    next_node.next = next_node.next.next

                else:
                    next_node = next_node.next #else go to the next node

            current_node = current_node.next#once the inner while loop is finished, increment by one node

        #checks the length of the modified linked lists, only return if length specification has been met
        size_linked_list = self.sizeOfLL()
        if 1 > size_linked_list or 100 < size_linked_list:
            raise Exception("sorry linked list out of range")

        else:
            return self.head



    # Merges all nodes from llist2 into the linked list object, maintains sorted order
    def merge(self, llist2):
        # TODO: Your Implementation Here

        current_list1_node = self.head #make reference of the head of list1 and list2 as well as create an empty list
        current_list2_node = llist2.head
        data_list = []

        while current_list1_node != None: # While untill reached the end of list1 then the last node will point to the head of list 2

            if current_list1_node.next == None:
                current_list1_node.next = current_list2_node
                break

            current_list1_node = current_list1_node.next

        current_list1_node = self.head

        while current_list1_node != None: #append each individual value of list1 into data_list list.
            data_list.append(current_list1_node.data)
            current_list1_node = current_list1_node.next

        data_list.sort()  # sort list
        count = 0

        for data in data_list: #update the value of each node in list1 with the sorted values from data_list
            self.updateNode(data,count)
            count += 1

        return self.head
        
def main():
    llist_nodes = input().split()
    if llist_nodes[0] == 'duplicate':
        llist = LinkedList()
        for i in range(1, len(llist_nodes)):
            llist.insertAtEnd(int(llist_nodes[i]))
        llist.remove_duplicates()
        llist.printLL()  
    else:
        llist1 = LinkedList()
        llist2 = LinkedList()
        llist2_index = llist_nodes.index("llist2")
        for i in range (1, llist2_index):
            llist1.insertAtEnd(int(llist_nodes[i]))
        for i in range(llist2_index + 1, len(llist_nodes)):
            llist2.insertAtEnd(int(llist_nodes[i]))
        llist1.merge(llist2)
        llist1.printLL()

if __name__ == "__main__":
    main()