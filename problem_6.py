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


# Set of elements which are in A, in B, or in both A and B
def union(llist_1, llist_2):
    all_elements = set()
    current_node = llist_1.head
    while current_node is not None:
        all_elements.add(current_node.value)
        current_node = current_node.next

    current_node = llist_2.head
    while current_node is not None:
        all_elements.add(current_node.value)
        current_node = current_node.next

    return all_elements


# Set of all objects that are members of both the sets A and B
def intersection(llist_1, llist_2):
    # Your Solution Here
    llist1_elements = set()
    intersect_elements = set()
    current_node = llist_1.head
    while current_node is not None:
        llist1_elements.add(current_node.value)
        current_node = current_node.next

    current_node = llist_2.head
    while current_node is not None:
        if current_node.value in llist1_elements:
            intersect_elements.add(current_node.value)
        current_node = current_node.next

    return intersect_elements


# Test case 1
# Duplicate values within each linked list
# Overlapping values between the two linked lists

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))  # Expected results: 3, 2, 35, 65, 6, 4, 21, 32, 9, 1, 11
print(intersection(linked_list_1, linked_list_2))  # Expected results: 4, 6, 21

# Test case 2
# Duplicate values within each linked list
# No overlapping values between the two linked lists (intersect should be empty)

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))


# Test case 3
# Both linked lists are empty
# Union and intersect should be empty

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

print(union(linked_list_5, linked_list_6))
print(intersection(linked_list_5, linked_list_6))
