import hashlib
import json


class Block:
    cnt = 0

    def __init__(self, index, timestamp, data, pre_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.pre_hash = pre_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + self.timestamp + self.pre_hash + \
            json.dumps(self.data) + str(self.cnt)
        encoded = data.encode()
        result = hashlib.sha256(encoded).hexdigest()
        return result

    def mine_block(self, difffcult):
        value = self.calculate_hash()
        temp = ""
        for x in range(0, difffcult):
            temp += "0"
        while value[0: difffcult] != temp:
            self.cnt += 1
            value = self.calculate_hash()
        print(self.cnt)
        self.hash = value
        return value


class Blockchain():
    difficult = 5

    def __init__(self):
        self.chain = self.create_root_block()

    def create_root_block(self):
        list_block = []
        list_block.append(Block(0, "1-12-2021",
                                {"trans1": "Thanh get 1000$ from cuu tro Covid"}))
        return list_block

    def get_latest_block(self):
        return self.chain[len(self.chain) - 1]

    def add_block(self, new_block):
        new_block.pre_hash = self.get_latest_block().hash
        new_block.hash = new_block.mine_block(Blockchain.difficult)
        self.chain.append(new_block)

    def check_valid(self):
        for x in range(1, len(self.chain)):
            if self.chain[x].hash != self.chain[x].calculate_hash():
                return False
            if self.chain[x].pre_hash != self.chain[x-1].calculate_hash():
                return False
        return True


block1 = Block(1, "1-12-2021",
               {"trans1": "Thanh get 11$ from cuu tro Covid"})
block2 = Block(2, "1-12-2021",
               {"trans2": "Thanh pay 10$ vaccine Covid"})
block3 = Block(3, "1-12-2021",
               {"trans2": "Thanh pay 1$ vaccine Covid"})
block_chain = Blockchain()
block_chain.add_block(block1)
block_chain.add_block(block2)
block_chain.add_block(block3)
print("Before:")
for block in block_chain.chain:
    print(str(block.index) + " " + block.hash + " " +
          json.dumps(block.data) + " " + block.pre_hash)

#block_chain.chain[1].data = {"trans1": "Thanh get 1$ from cuu tro Covid"}
#block_chain.chain[1].hash = block_chain.chain[1].calculate_hash()
# print("After: ")
# print(block_chain.check_valid())
# for block in block_chain.chain:
#     print(str(block.index) + " " + block.hash + " " +
#           json.dumps(block.data) + " " + block.pre_hash)
