
from api.blockchain import Blockchain, create_block, hash_block, prepare_proof, proof_of_work

import pytest
import datetime
from freezegun import freeze_time


@freeze_time("2024-05-21T14:41:37")
def test_time():
    expected_time = datetime.datetime(
        2024, 5, 21,
        14, 41, 37)
    actual_time = datetime.datetime.now()
    assert actual_time == expected_time

@pytest.fixture
def block():
    return create_block("test data", 100, "abcd1234", 2)

@pytest.fixture
@freeze_time("2024-05-21T14:41:37")
def blockchain():
    return Blockchain()


@freeze_time("2024-05-21T14:41:37")
def test_init(blockchain):
    """Test initialization of the blockchain and the creation of the genesis block."""
    assert len(blockchain.chain) == 1
    assert blockchain.chain[0]['data'] == 'genesis block'
    assert blockchain.chain[0]['index'] == 1
    assert blockchain.chain[0]['proof'] == 1
    assert blockchain.chain[0]['previous_hash'] == '0'
    assert blockchain.chain[0]['timestamp'] == datetime.datetime.now().isoformat()


def test_create_block(block):
    """Test the create_block method to ensure it returns a correct block structure."""
    assert block['data'] == "test data"
    assert block['proof'] == 100
    assert block['previous_hash'] == "abcd1234"
    assert block['index'] == 2
    assert 'timestamp' in block


def test_mine_block(blockchain):
    """Test mining a new block to see if it is added to the chain correctly."""
    new_block = blockchain.mine_block("mine this block")
    assert len(blockchain.chain) == 2  # includes genesis block
    assert new_block in blockchain.chain


def test_hash_block(blockchain, block):
    """Test the hash_block method to check if it generates the expected hash."""
    hashed = hash_block(block)
    assert type(hashed) is str
    assert len(hashed) == 64  # Length of a SHA-256 hash in hex


def test_proof_of_work(blockchain):
    """Test the proof_of_work method to ensure it finds a correct proof."""
    previous_proof = blockchain.chain[-1]['proof']
    new_proof = proof_of_work(previous_proof, 2, "some data")
    assert new_proof is not None
    assert isinstance(new_proof, int)


def test_prepare_proof(blockchain):
    """Test the prepare_proof method to ensure it prepares correct string for hashing."""
    prepared = prepare_proof(2, 1, 2, "test")
    assert prepared == b'5test'


def test_get_previous_block(blockchain):
    """Test get_previous_block to ensure it returns the last block in the chain."""
    last_block = blockchain.get_previous_block()
    assert last_block == blockchain.chain[-1]


def test_is_chain_valid(blockchain):
    """Test is_chain_valid to ensure it correctly validates the blockchain."""
    # Valid chain
    blockchain.mine_block("block 2")
    assert blockchain.is_chain_valid() is True

    # Invalidate the chain by tampering with a block
    blockchain.chain[1]['data'] = "tampered data"
    assert blockchain.is_chain_valid() is False
