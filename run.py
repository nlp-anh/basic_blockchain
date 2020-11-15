from blockchain import Blockchain

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

fake_transaction = {"sender": "Bob",
                    "receiver": "Cole, Alice",
                    "amount": 25}

myBlockchain = Blockchain()
myBlockchain.print_blocks()

myBlockchain.add_block(transaction1)
myBlockchain.add_block(transaction2)
myBlockchain.add_block(transaction3)
myBlockchain.add_block(transaction4)
myBlockchain.print_blocks()

# Replace a block with a fake transaction
myBlockchain.chain[2].transactions = fake_transaction
myBlockchain.validate_chain()
