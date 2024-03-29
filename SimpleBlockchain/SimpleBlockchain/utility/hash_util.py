import hashlib as hl
import json

def hash_string_256(string):
    """Creates a SHA256 hash for a given input string.

    Arguments:
        :string: The string which should be hashed.
    """
    return hl.sha256(string).hexdigest()

def hash_block(block):
    """Hashes a block and returns a string representation of it.

    Arguments:
        :block: The block that should be hashed.
    """
    hashable_block = block.__dict__.copy()
    hashable_block["transactions"] = [tx.to_ordered_dict() for tx in hashable_block["transactions"]]
    json_block = json.dumps(hashable_block, sort_keys=True)
    encoded_json_block = json_block.encode()
    return hash_string_256(encoded_json_block)
