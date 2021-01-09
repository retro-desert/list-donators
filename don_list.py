from web3 import Web3
import json

infura_url = "https://rinkeby.infura.io/" # Input your own API
web3 = Web3(Web3.HTTPProvider(infura_url))

contract_address = "" # Input your own address
contract_abi = [
	{
		"stateMutability": "payable",
		"type": "receive"
	},
	{
		"inputs": [],
		"name": "allDonatorsList",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "list",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

print("Donators list:")
s = contract.functions.allDonatorsList().call().split(" ")
for i in s:
	if i == "":
		s.remove(i)
		continue
	s[s.index(i)] = Web3.toChecksumAddress(str(i))
print(s)
