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
