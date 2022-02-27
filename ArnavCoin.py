import hashlib

# Declaring what a block looks like on the blockchain
# Contains: Information about: 1. Hash of previous block, 2. It's own hash, 3. List of transactions,
# 4. Data on the block which is a concatenated string with transaction on the list and hash of previous block,
# separated by '-'
class ArnavCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash

        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Arnav sends 2 AC to Agastya"
t2 = "Arnav sends 2 AC to Olwen"
t3 = "Arnav sends 1.5 AC to Harry Potter"
t4 = "Harry Potter sends 1 AC to Hermione Granger"
t5 = "Hermione Granger sends 0.75 SC to Olwen"
t6 = "Olwen sends 0.75 AC to Ron Weasley"

# Creating 1st block for the blockchain, i.e genesis block and 1st transactions.
genesis_block = ArnavCoinBlock("Genesis Block", [t1, t2])
print(genesis_block.block_data)
print(genesis_block.block_hash)

# Creating block 2 for blockchain using hash of genesis block and next 2 transactions.
block_2 = ArnavCoinBlock(genesis_block.block_hash, [t3, t4])
print(block_2.block_data)
print(block_2.block_hash)

# Creating block 3 for blockchain using hash of block 1 and next 2 transactions.
block_3 = ArnavCoinBlock(block_2.block_hash, [t3, t4])
print(block_3.block_data)
print(block_3.block_hash)

# Can run "python3 ArnavCoin.py" to see what the outputs are.
