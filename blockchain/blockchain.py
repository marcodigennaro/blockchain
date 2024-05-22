import datetime as dt
import hashlib as hl
import json


def create_block(data: str, proof: int, previous_hash: str, index: int) -> dict:
    """Create a new block and return it."""
    block = {
        "index": index,
        "timestamp": dt.datetime.now().isoformat(),
        "data": data,
        "proof": proof,
        "previous_hash": previous_hash
    }
    return block


def hash_block(block: dict) -> str:
    """Create a SHA-256 hash of a block."""
    encoded_block = json.dumps(block, sort_keys=True).encode()
    return hl.sha256(encoded_block).hexdigest()


def prepare_proof(new_proof: int, previous_proof: int, index: int, data: str) -> bytes:
    """Prepare data string for hashing to find new proof."""
    proof_string = f"{new_proof ** 2 - previous_proof ** 2 + index}{data}"
    return proof_string.encode()


def proof_of_work(previous_proof: int, index: int, data: str) -> int:
    """Simple Proof of Work algorithm."""
    new_proof = 1
    check_proof = False
    while not check_proof:
        to_digest = prepare_proof(new_proof, previous_proof, index, data)
        hash_value = hl.sha256(to_digest).hexdigest()
        if hash_value[:4] == "0000":
            check_proof = True
        else:
            new_proof += 1
    return new_proof


class Blockchain:
    def __init__(self) -> None:
        """Initialize the blockchain with the genesis block."""
        self.chain = []
        genesis_block = create_block(
            data="genesis block",
            proof=1,
            previous_hash="0",
            index=1
        )
        self.chain.append(genesis_block)

    def mine_block(self, data: str) -> dict:
        """Mine a new block with the provided data and add it to the blockchain."""
        previous_block = self.get_previous_block()
        previous_proof = previous_block["proof"]
        index = len(self.chain) + 1
        proof = proof_of_work(previous_proof, index, data)
        previous_hash = hash_block(previous_block)
        new_block = create_block(data=data, proof=proof, previous_hash=previous_hash, index=index)
        self.chain.append(new_block)
        return new_block

    def get_previous_block(self) -> dict:
        """Get the last block in the blockchain."""
        return self.chain[-1]

    def is_chain_valid(self) -> bool:
        """Check if the blockchain is valid."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i - 1]
            next_block = self.chain[i]
            if next_block["previous_hash"] != hash_block(current_block):
                return False

            current_proof = current_block["proof"]
            next_proof = next_block["proof"]
            data_string = prepare_proof(next_proof, current_proof, next_block["index"], next_block["data"])
            hash_value = hl.sha256(data_string).hexdigest()

            if hash_value[:4] != "0000":
                return False

        return True
