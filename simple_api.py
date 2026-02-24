from flask import Flask, request, render_template, redirect, url_for
import requests
import json
from simple_blockchain import SimpleBlockchain 
 
# adapted from: https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/

app = Flask(__name__)

blockchain = SimpleBlockchain()


# Web GUI index page
@app.route('/')
def index():
    chain_data = [block.__dict__ for block in blockchain.chain]
    return render_template('index.html', chain=chain_data)

# Add transaction via form
@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    sender = request.form['sender']
    recipient = request.form['recipient']
    amount = request.form['amount']
    blockchain.add_new_transaction({
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    })
    blockchain.mine()
    return redirect(url_for('index'))

# API endpoint for chain (unchanged)
@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = [block.__dict__ for block in blockchain.chain]
    return json.dumps({"length": len(chain_data), "chain": chain_data})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
