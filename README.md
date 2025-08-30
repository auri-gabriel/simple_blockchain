# Simple Blockchain

A basic blockchain implementation in Python with a REST API interface. This project demonstrates fundamental blockchain concepts including block creation, proof-of-work consensus, and transaction handling.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/auri-gabriel/simple-blockchain.git
cd simple-blockchain
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the API Server

Start the Flask development server:

```bash
python simple_api.py
```

The server will start on `http://localhost:5000`

### API Endpoints

#### Get Blockchain

- **Endpoint**: `GET /chain`
- **Description**: Returns the complete blockchain with all blocks
- **Response**: JSON object containing the chain length and all blocks

Example:

```bash
curl http://localhost:5000/chain
```

## Educational Purpose

This implementation is designed for educational purposes to demonstrate:

- Basic blockchain concepts
- Proof-of-work consensus mechanism
- Block validation and chain integrity
- Simple transaction handling

**Note**: This is a simplified implementation and should not be used in production environments.

## Acknowledgments

Adapted from: [ActiveState - How to Build a Blockchain in Python](https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/)
