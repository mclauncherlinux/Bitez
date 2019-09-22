Bitez: Self hosted cryptocurrency wallet as a service
==============================================

**Bitez** _(pronounced Bit Easy)_ is a self hosted cryptocurrency wallet server you can use to create BTC/BCH wallets and perform multiple operations such as transactions and wallets generation with a simple HTTP interface.

You will need mongodb to store wallets, user accounts and api keys. Of course, private keys are encrypted before getting stored.

I created **Bitez** because I wanted a free alternative to [Block.io](https://block.io/).

Installation
------------
First, you'll need to install all the dependencies:
```bash
# using pip
pip install requirements.txt

# or using Pipenv
pipenv install
```
Then you'll need to create a file at the root directory called (`.env`) with the following vars to store your secret environnement variables:
```bash
DB_HOST='<mongodb URI>'
DB_PORT='<mongodb port>'
DB_CLIENT='<mongodb client>'
SECRET_KEY='<random string used for jwt salting>'
MAIL_SERVER='<email smtp server>'
MAIL_PORT='<email smtp server port>'
MAIL_USERNAME='<email address for account activation>'
MAIL_PASSWORD='<password for accessing email account>'
ENCRYPTION_SECRET='<random string used for jwt salting>'
```
After saving the file, start the server with one of the following commands:
```bash
# mainnet server
python main.py

# or

# testnet server
python main.py --dev

# or

# mainnet production server
gunicorn main:app
```

Guide
------------
### Before accessing the API, the client needs to create an account. Go to `/` on your web browser and click on register then login and generate an API key.

# 

### Generate a new address:
```bash
# BTC
GET /api/btc/generate?api_key=<API_KEY>

# BCH
GET /api/bch/generate?api_key=<API_KEY>
```

### Get all addresses:
```bash
# BTC
GET /api/btc/addresses?api_key=<API_KEY>

# BCH
GET /api/bch/addresses?api_key=<API_KEY>
```

### Get wallet balance:
```bash
# BTC
GET /api/btc/balance?api_key=<API_KEY>&currency=<CURRENCY>

# BCH
GET /api/bch/balance?api_key=<API_KEY>&currency=<CURRENCY>

# available currencies: btc, bch, usd, eur, gbp, jpy and other major currencies like cad and chf
```

### Get transaction history:
```bash
# BTC
GET /api/btc/history?api_key=<API_KEY>

# BCH
GET /api/bch/history?api_key=<API_KEY>
```

### Get current rates:
```bash
# BTC
GET /api/btc/rates?api_key=<API_KEY>&currency=<CURRENCY>

# BCH
GET /api/bch/rates?api_key=<API_KEY>&currency=<CURRENCY>

# available currencies: btc, bch, usd, eur, gbp, jpy and other major currencies like cad and chf
```

### Get a fiat amount in crypto:
```bash
# BTC
GET /api/btc/rates?api_key=<API_KEY>&currency=<CURRENCY>&amount=<AMOUNT>

# BCH
GET /api/bch/rates?api_key=<API_KEY>&currency=<CURRENCY>&amount=<AMOUNT>

# available currencies: btc, bch, usd, eur, gbp, jpy and other major currencies like cad and chf
```

### Check if an address is valid:
```bash
# BTC
GET /api/btc/validate?api_key=<API_KEY>&address=<ADDRESS>

# BCH
GET /api/bch/validate?api_key=<API_KEY>&address=<ADDRESS>
```

### Perform a transaction:
```bash
# BTC
POST /api/btc/tx?api_key=<API_KEY> {
    "recipient":"<ADDRESS>",
    "amount": <AMOUNT>,
    "currency": "<CURRENCY>"
}

# BCH
POST /api/bch/tx?api_key=<API_KEY> {
    "recipient":"<ADDRESS>",
    "amount": <AMOUNT>,
    "currency": "<CURRENCY>"
}

# available currencies: btc, bch, satoshi, usd, eur, gbp, jpy and other major currencies like cad and chf
```

Donate
------------

Based on community needs, I will keep improving the project and adding new functionalities. You can help me do that by **contributing** to the project or by **donating** a little something to encourage me.

**Donate BTC:** 1HHMRuezg1WAPqGRQ3S8xFKGgmMHZZrCoa

**Donate BCH:** bitcoincash:qrxjktfjdse3ll0ttrll20gykuhqjw764queg3w2tj

**Donate Love:** Just [tweet](https://twitter.com/merwanedr) me something cool :)

Contributing
------------
If you like **Bitez** and want to contribute to it, you can make a pull request on a new branch wether it is for a bugfix or for a new feature. 

You can also request a feature or report a bug by using Github issues, or by dropping me an [email](mailto:merwanedr@gmail.com).

Promoting the project is also considered a huge contribution! Any action is welcome as long as it helps **Bitez** grow! 

Notes and credits
------------
* I really wanted to thank [Ofek Lev](https://github.com/ofek) for his library [bit](https://github.com/ofek/bit) and [Sporestack](https://github.com/sporestack) with his fork [bitcash](https://github.com/sporestack/bitcash) which made **Bitez** possible without me having a headache!