# Multi-Blockchain-Wallet

There are so many crypto coins out there so that there is a need to build out a system which can create them. Here is a command line tool, hd-wallet-derive that supports not only BIP32, BIP39, and BIP44, but also supports non-standard derivation paths for the most popular wallets out there today. Alos, python script has been integrated to act as "Universal" wallet which can manage billions of addresses across 300+ coins.
As a prototype, system has been tested for Ethereum and Bitcoin Testnet.

## Environment Setup

PHP 7.4.26 and Python 3.8.3 has been installed first. Then rest of the dependencies can be installed using requirements.txt file in the repo.

`pip install -r requirements.txt`

## Installing the hd-wallet-derive

After clone this repo, cd into the repo. Then, open a Git Bash terminal with administrator rights and execute each of below commands.

```
git clone https://github.com/dan-da/hd-wallet-derive
cd hd-wallet-derive
curl https://getcomposer.org/installer -o installer.php
php installer.php
php composer.phar install
```

If all setup correctly, run the below command and output should be as below.

`./derive --key=xprv9zbB6Xchu2zRkf6jSEnH9vuy7tpBuq2njDRr9efSGBXSYr1QtN8QHRur28QLQvKRqFThCxopdS1UD61a5q6jGyuJPGLDV9XfYHQto72DAE8 --cols=path,address --coin=ZEC --numderive=3 -g`

<p align="center">
  <img src="https://github.com/chirathlv/Multi-Blockchain-Wallet/blob/main/Images/Link%20Test.PNG">
</p>

## Derive the wallet keys

Included print function in the wallet.py file will print out 3 accounts for each ETH and BTCTEST based on the mnemonic in the .env file.

<p align="center">
  <img src="https://github.com/chirathlv/Multi-Blockchain-Wallet/blob/main/Images/Derive%20Wallet%20Keys.PNG">
</p>

## Bitcoin Testnet transaction

Within the Python shell, run below commands

```
from wallet import *
acc = priv_key_to_account('btc-test', 'cVAgDoahzo5Ucdv8ioxxubvmE6LfU3ZQgJ21UvY4eC1xi6WkvnXe')
send_tx('btc-test', acc, 'cVAgDoahzo5Ucdv8ioxxubvmE6LfU3ZQgJ21UvY4eC1xi6WkvnXe', 0.000005)
```

<p align="center">
  <img src="https://github.com/chirathlv/Multi-Blockchain-Wallet/blob/main/Images/btc-test%20transaction.PNG">
</p>

### Bitcoin Testnet transaction confirmation

<p align="center">
  <img src="https://github.com/chirathlv/Multi-Blockchain-Wallet/blob/main/Images/btc-test%20transaction%20confirmation.PNG">
</p>
