import sys
from collections import deque


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

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def get_value(self):
        return self.value

    def __repr__(self):
        return str(self.value)


class Tree:
    def __init__(self, root):
        self.root = root

    def get_root(self):
        return self.root


class Queue:
    def __init__(self):
        self.q = deque()

    def enq(self, node, code):
        self.q.appendleft([node, code])

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)


# Method for encoding an input string
# Input: data (string) - string to encode
# Output: encoded_data (string) - encoded string
#         huffman_tree (Tree) - tree structure for decoding
def huffman_encoding(data):
    # Edge case 1: Empty string
    if data == "":
        return "0", None
    # Based on string, get frequency of each character
    character_frequency = dict()
    for character in data:
        if character in character_frequency:
            character_frequency[character] += 1
        else:
            character_frequency[character] = 1

    # Sort by frequency (descending so that we can pop the least frequent)
    character_frequency_sorted = sorted(character_frequency.items(),
                                        key=lambda dictionary: dictionary[1],
                                        reverse=True)

    # Store created nodes here
    node_storage = dict()  # Contains <Character string, Node>

    # Follow algorithm for building tree
    # Reference: https://www.siggraph.org/education/materials/HyperGraph/video/mpeg/mpegfaq/huffman_tutorial.html

    # Keep combining and resorting until there is only one entry left
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

        # Do the same for the right child (check if node already exists)
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

    # Edge case 2: Input string contains only one character (example: 'aaaaaa')
    if len(node_storage) == 0:
        huffman_tree = Tree(Node(character_frequency_sorted[0][0]))
    else:
        # Create the tree with the remaining node
        huffman_tree = Tree(node_storage[character_frequency_sorted[0][0]])

    # Create a dictionary of character and encoded value for character
    encoding_information = build_encoding(huffman_tree)
    encoded_data = data

    # Build the encoded string
    for entry in reversed(encoding_information):
        encoded_data = encoded_data.replace(entry[0], entry[1])
    return encoded_data, huffman_tree


# Method for decoding an input string
# Input: data (string) - string to decode
#        tree (Tree) - Huffman tree used to encode string
# Output: decoded_string (string) - decoded string
def huffman_decoding(data, tree):
    # Case 1: Input was blank ("")
    if data == "0":
        return ""
    decoding_information = build_encoding(tree)
    decoded_string = data
    for item in reversed(decoding_information):
        decoded_string = decoded_string.replace(item[1], item[0])
    return decoded_string


# Helper function for generating codes for each character based on the provided tree to be used in encoding/decoding
def build_encoding(tree):
    character_codes = list()
    q = Queue()

    # start at the root node and add it to the queue
    node = tree.get_root()
    q.enq(node, '01')
    while len(q) > 0:
        node, code = q.deq()
        if node.has_left_child():
            q.enq(node.get_left_child(), code + '0')
        if node.has_right_child():
            q.enq(node.get_right_child(), code + '11')
        if not node.has_left_child() and not node.has_right_child():
            character_codes.append([node.get_value(), code])
    return character_codes


if __name__ == "__main__":
    codes = {}

    # Case 1: Normal sentence
    # Case 2: Another normal sentence
    # Case 3: (Edge case) Blank input ""
    # Case 4: (Edge case) Repeated same character "aaaaa"

    sentences_to_encode = ["The bird is the word", "Here is a sentence to encode", "", "aaaaa"]

    for a_great_sentence in sentences_to_encode:
        print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print("The content of the data is: {}\n".format(a_great_sentence))

        encoded_data, tree = huffman_encoding(a_great_sentence)

        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))
