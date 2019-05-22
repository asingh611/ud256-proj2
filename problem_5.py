import hashlib
from datetime import datetime

class Block:
    def __init__(self, data, previous_hash=None, previous_block=None):
      self.timestamp = datetime.utcnow() #  Returns current timestamp in UTC (GMT) timezone
      self.data = data
      self.previous_hash = previous_hash
      self.previous_block = previous_block
      self.hash = self.calc_hash()

    # Uses SHA256 to generate hash based on the data and timestamp
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        hash_timestamp = str(self.timestamp).encode('utf-8')
        hash_previousHash = str(self.previous_hash).encode('utf-8')
        sha.update(hash_str)
        sha.update(hash_timestamp)
        sha.update(hash_previousHash)
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def append(self, data):
        if self.head is None:
            self.head = Block(data)
            self.tail = self.head
            self.size += 1
        else:
            new_block = Block(data, self.tail.hash, self.tail)
            self.tail = new_block
            self.size += 1

    def print_chain(self):
        block_to_print = self.tail
        while block_to_print is not None:
            print("Data: " + block_to_print.data)
            print("Hash: " + block_to_print.hash)
            previous_hash = "(None)"
            if block_to_print.previous_hash is not None:
                previous_hash = block_to_print.previous_hash
            print("Previous Hash: " + previous_hash)
            print("-------------------------------------")
            block_to_print = block_to_print.previous_block


bc = Blockchain()
bc.append("This is my cryptocurrency AndyCoin")     # Case 1: adding data normally
bc.append("This is my cryptocurrency AndyCoin")     # Case 2: adding block same data string as previous block
bc.append("")                                       # Case 3: adding empty string
bc.print_chain()
