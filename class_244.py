from web3 import Web3
from web3.middleware import geth_poa_middleware 

API_url = 'https://mainnet.infura.io/v3/1a3c50f1e38044fd9e869249ed8bbba1' #student will add this
web3 = Web3(Web3.HTTPProvider(API_url)) 

Block_data = web3.eth.getBlock(16433106) # any block can be taken

#print('transaction data',Block_data['transactions']) 
transaction = web3.eth.get_transaction('0xb29d7d2715905242f5e1ef47b40f54e0c0895d7be9f44f498aab539ab6883a0e')

print('blockHash:',transaction['blockHash'].hex())
print('blockNumber:',transaction['blockNumber'])
print('from:',transaction['from'])
print('gas:',transaction['gas'])
print('gasPrice in ether:',transaction['gasPrice'])
print('hash:',transaction['hash'].hex())
print('input:',transaction['input'])
print('nonce:',transaction['nonce'])
print('signature:',transaction['s'].hex())
print('to:',transaction['to'])
print('value:',transaction['value'])