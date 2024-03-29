# Import dependencies
import subprocess
import json
import os
from dotenv import load_dotenv
from constants import *
from web3 import Web3
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI
from web3.middleware import geth_poa_middleware

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")

# Intantiating a web3 instance
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Create a function called `derive_wallets`
def derive_wallets(coin):
    command = f'php ./derive -g --mnemonic=mnemonic --coin={coin} --numderive=3 --cols=path,address,privkey,pubkey --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {'eth': derive_wallets(ETH), 'btc-test': derive_wallets(BTCTEST)}

print(json.dumps(coins, indent=4, separators=(',', ': ')))
#print(coins[ETH][0]['privkey'])

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
    
    if coin==ETH:
        return w3.eth.account.privateKeyToAccount(priv_key)
    elif coin==BTCTEST:
        return PrivateKeyTestnet(priv_key)

print(priv_key_to_account(ETH, coins[ETH][0]['privkey']))
# print(priv_key_to_account(BTCTEST, coins[BTCTEST][0]['privkey']))

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin, account, to, amount):
    if coin==ETH:
        gasEstimate = w3.eth.estimateGas(
            {"from": account.address, "to": to, "value": amount}
        )
        return {
            "from": account.address,
            "to": to,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address),
            "chainId": 1337 #Geth private chains (default) - https://github.com/ethereum/EIPs/blob/master/EIPS/eip-155.md
        }
    elif coin==BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, 'btc')])

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin, account, to, amount):
    raw_tx = create_tx(coin, account, to, amount)
    signed_tx = account.sign_transaction(raw_tx)
    if coin==ETH:
        return w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    elif coin==BTCTEST:
        return NetworkAPI.broadcast_tx_testnet(signed_tx)
