import sys


# Add Node and Tree classes
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def __repr__(self):
        return str(self.value)


class Tree:
    def _init_(self, root):
        self.root = root


def huffman_encoding(data):
    # Need to decide what the results would be for the edge cases

    # Based on string, get frequency of each character
    character_frequency = dict()
    for character in data:
        if character in character_frequency:
            character_frequency[character] += 1
        else:
            character_frequency[character] = 1

    # Sort by frequency (descending so that we can pop the least frequent)
    # TODO: Check if you can use a sorted dictionary (need to review time complexity)
    character_frequency_sorted = sorted(character_frequency.items(),
                                        key=lambda dictionary: dictionary[1],
                                        reverse=True)

    # Store created nodes here
    node_storage = dict()  # Contains <Character string, Node>

    # Follow algorithm for building tree
    # Reference: https://www.siggraph.org/education/materials/HyperGraph/video/mpeg/mpegfaq/huffman_tutorial.html

    while len(character_frequency_sorted) >= 2:
        # Get the two least frequent characters
        least_frequent = character_frequency_sorted.pop()
        next_least_frequent = character_frequency_sorted.pop()
        parent_node = Node()

        # If there is a node created for this character string already
        if least_frequent[0] in node_storage:
            # Set it equal to the existing child node
            parent_node.set_left_child(node_storage[least_frequent[0]])
        else:
            # Otherwise create a new child node
            parent_node.set_left_child(Node(least_frequent[0]))

        # Do the same for the right child
        if next_least_frequent[0] in node_storage:
            parent_node.set_right_child(node_storage[next_least_frequent[0]])
        else:
            parent_node.set_right_child(Node(next_least_frequent[0]))

        parent_node.value = parent_node.get_left_child().value + parent_node.get_right_child().value

        parent_frequency_values = least_frequent[1] + next_least_frequent[1]

        node_storage[parent_node.value] = parent_node
        character_frequency_sorted.append((parent_node.value, parent_frequency_values))

        character_frequency_sorted = sorted(character_frequency_sorted,
                                            key=lambda frequency_tuple: frequency_tuple[1],
                                            reverse=True)


    # Now that you have two nodes left, create the tree with the root node having the two remaining nodes

    # Traverse tree and for each leaf, store key/value -> key = character; value = encoded
    # Encode string one character at a time
    # Return the encoded string and tree

    pass


def huffman_decoding(data, tree):
    pass


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
