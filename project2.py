

from lxml import html
import requests
import random
import sys
from colorama import Fore, Style
from hdwallet import HDWallet
from hdwallet.symbols import ETH as SYMBOL


z = 3200000000000000001
while True:
    magic = "0000000000000000000000000000000000000000000000000000000000000000"
    while len(magic) < 64:
        magic = magic + "0"
    magic = magic[:64-len(str(hex(z)[2:]))] + str(hex(z)[2:])
    PRIVATE_KEY = str(magic)
    hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
    hdwallet.from_private_key(private_key=PRIVATE_KEY)
    privatekey = hdwallet.private_key()
    ethaddr = hdwallet.p2pkh_address()
    f = open('eth.txt', "r")

    while line := f.readline():
            print(line[:42] , str.lower(ethaddr) , privatekey)
            if str.lower(ethaddr) == line[:42] :
              print('Write Information Wallet On File Winner (MMDRZA.Com)')
              print('==========================[Mmdrza.Com]================================')
              print('WINNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR')
              fileone = open("ethATOMICWINEEEEEEERRRRRRRRRRRRRRRRRRRRRRR.txt","a")
              fileone.write('\nADDRESS ETH      : ' + ethaddr)
              fileone.write('\nPrivate Key ETH   : ' + privatekey)
              fileone.write('\nValue TX   ETH   : ' )
              fileone.write('\n=====================[ MMDRZA.CoM ]===========================\n')
              fileone.close()
              print('Saved and Write All Details For WiN Wallet')
              continue
    f.close()
    print(z)
    z +=1    
