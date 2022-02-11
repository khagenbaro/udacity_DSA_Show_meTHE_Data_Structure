

from cgi import print_directory
import re
from unittest import result


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    #declaring the method which convert the linked list to set
    def to_set(self):
        l_set =set()
        n = self.head
        while n:
            l_set.add(n.value)
            n = n.next
        return l_set


def union(llist_1, llist_2):
    # My Solution Here

    setoflinkedlist1= llist_1.to_set() #converting linkedlist to set
    setoflinkedlist2 = llist_2.to_set() #converting linkedlist to set
    
    union = set() #creating a new empty set
    
    #union logic in the sets of the linked lists
    union = setoflinkedlist1 | setoflinkedlist2
    return union



def intersection(llist_1, llist_2):
    # My Solution Here

    set_of_linked_list_1 = set()  #creating an empty set to store all the non duplicate values of the first linkedlist 
    current_node = llist_1.head
    #traversing through the linked list and adding into set above declared
    while current_node:
        set_of_linked_list_1.add(current_node.value)
        current_node = current_node.next
    #creating an empty set to store all the non duplicate values of the second linked list 
    set_of_linked_list_2 = set()
    current_node = llist_2.head

    #traversing through linked list and storing intoo the set
    while current_node:
        set_of_linked_list_2.add(current_node.value)
        current_node = current_node.next
    set_of_linked_list_2_head = Node(None)
    set_of_linked_list_2_node = set_of_linked_list_2_head

    intersection_set = set_of_linked_list_1.intersection(set_of_linked_list_2)
    return intersection_set


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print('\n test case 1:\n')
print('union is : ')
print(union(linked_list_1,linked_list_2))
print('\n')
print('Intersection is : ')
print(intersection(linked_list_1,linked_list_2))
print('\n')
# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)
print('test case 2:\n')
print('union is : ')
print (union(linked_list_3,linked_list_4))
print('\n')
print('Intersection is : ')
print (intersection(linked_list_3,linked_list_4))
print('\n')

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_5 = [1,1,1,1]
element_6 = [1,2,2,1]

for i in element_5:
    linked_list_5.append(i)

for i in element_6:
    linked_list_6.append(i)
print('test case 3:\n')
print('union is : ')
print (union(linked_list_5,linked_list_6))
print('\n')
print('Intersection is : ')
print (intersection(linked_list_5,linked_list_6))
print('\n')