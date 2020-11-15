# BLOCKCHAIN TECHNOLOGY

Blockchain is a way of storing and moving data which can be in any form, such as money, contracts, messages, etc. A transaction typically consists of a sender, a receiver and the  data (the amount of money), which can be stored in a Python dictionary.

For example:
```Python
transaction1 = {"sender": "Ashton",
                "receiver": "Emile",
                "amount": 530}

transaction2 = {"sender": "Jett",
                "receiver": "Xena",
                "amount": 295}

transaction3 = {"sender": "Payne",
                "receiver": "Mitchel",
                "amount": 447}

transaction4 = {"sender": "Chelsie",
                "receiver": "Taylor",
                "amount": 947}

```

All these transactions are stored in a memory pool or mempool in short.

```Python
mempool = [transaction1, transaction2, transaction3, transaction4]
```

A miner will select a set or a block of transactions from this pool to verify before adding to the blockchain structure.

```python
transactions_block = [mempool[0], mempool[1]]
```

Since blocks can be represented as objects, we can describe a Block class and use it to create new blocks. A block in the blockchain contains: timestamp, transactions, hash, previous hash and a nonce.

As you can see, each block has its own unique hash which helps to maintain the integrity in the blockchain. Here, the SHA256 algorithm is implemented to produce the hash of the block using the timestamp, data, the hash of the previous block and a nonce.

What is nonce? Nonce is a a random number that can be used only for one time. Noted that this number is predetermined. Therefore, the mining process in blockchain aims to find the value of nonce, so that the block hash value satisfies a target difficulty. Once it's done, the miners will get reward for their efforts.

Now we have a block. We can add this block to the blockchain. Each participant in the network has their own replicate of the blockchain. Each of these replicates share the similar properties and functions. Therefore, we can describe the blockchain as an object. Any blockchain object has:  
- a chain: a list that stores all the blocks of the blockchain
- unverified transactions: a list of unverified transactions before being added into a block
- genesis block: the very first block that is automatically generated at the initialisation step of the blockchain
