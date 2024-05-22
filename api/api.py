import fastapi
from blockchain.blockchain import Blockchain

bc = Blockchain()
app = fastapi.FastAPI()


# endpoints to mine a block
@app.post("/mine_block/")
def mine_block(data: str):
    if not bc.is_chain_valid():
        return fastapi.HTTPException(status_code=400, detail="Invalid Blockchain")

    block = bc.mine_block(data=data)


# endpoints to return the whole chain
@app.post("/blockchain/")
def get_blockchain(data: str):
    if not bc.is_chain_valid():
        return fastapi.HTTPException(status_code=400, detail="Invalid Blockchain")

    chain = bc.chain
    return chain


# endpoint to see if the blockchain is valid
@app.get("/validate/")
def is_valid():
    return bc.is_chain_valid()

#endpoint to return previous block
@app.get("/previous_block/")
def previous_block():
    if not bc.is_chain_valid():
        return fastapi.HTTPException(status_code=400, detail="Invalid Blockchain")
    return bc.get_previous_block()