from flask import Flask, request
import requests
import json
from simple_blockchain import SimpleBlockchain 
 
# adapted from: https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/

app =  Flask(__name__)

blockchain = SimpleBlockchain()

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})
app.run(debug=True, port=5000)
