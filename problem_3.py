import sys

def huffman_encoding(data):
    # Based on string, get frequency of each character
    character_frequency = dict()
    for character in data:
        if character in character_frequency:
            character_frequency[character] += 1
        else:
            character_frequency[character] = 1

    # Sort by frequency
    character_frequency_sorted = sorted(character_frequency.items(), key=lambda dictionary: dictionary[1])

    # Follow algorithm for building tree
    # Reference: https://www.siggraph.org/education/materials/HyperGraph/video/mpeg/mpegfaq/huffman_tutorial.html


    # Traverse tree and for each leaf, store key/value -> key = character; value = encoded
    # Encode string one character at a time
    # Return the encoded string and tree

    pass

def huffman_decoding(data,tree):
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
