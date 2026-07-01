# Binance Futures Testnet Trading Bot

A Python-based CLI application that places **Market** and **Limit** orders on the **Binance USDT-M Futures Testnet**. The application is designed with a modular structure, input validation, logging, and exception handling.

---

## Features

- Place **Market Orders**
- Place **Limit Orders**
- Supports **BUY** and **SELL**
- Command Line Interface (CLI)
- Input validation
- API request/response logging
- Exception handling for invalid input, API errors, and network failures
- Modular and reusable code structure

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── .env.example
├── cli.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Requirements

- Python 3.10+
- Binance Futures Testnet Account
- Binance Futures Testnet API Key & Secret

---

## Installation

Clone the repository:

```bash
git clone <https://github.com/tanmmayyy/binance_trading_bot>
cd trading_bot
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root.

Example:

```env
API_KEY=YOUR_BINANCE_TESTNET_API_KEY
API_SECRET=YOUR_BINANCE_TESTNET_API_SECRET
```

You can generate your API credentials from the Binance Futures Testnet.

---

## Running the Application

### Market BUY

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Market SELL

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

### Limit BUY

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

### Limit SELL

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 80000
```

---

## Sample Output

```
========== ORDER SUMMARY ==========
Symbol : BTCUSDT
Side : BUY
Type : MARKET
Quantity : 0.001

========== RESPONSE ==========
Order ID : 123456789
Status : FILLED
Executed Qty : 0.001
Avg Price : 108250.30

SUCCESS
```

---

## Logging

All API requests, responses, and errors are recorded in:

```
logs/trading.log
```

---

## Error Handling

The application handles:

- Invalid order side
- Invalid order type
- Invalid quantity
- Missing limit price
- Binance API exceptions
- Network failures
- Unexpected runtime exceptions

---

## Assumptions

- The Binance Futures Testnet account is activated.
- Valid Testnet API credentials are provided.
- The trading symbol exists on Binance Futures Testnet.
- The account has sufficient Testnet balance.

---

## Dependencies

- python-binance
- python-dotenv

Install using:

```bash
pip install -r requirements.txt
```

---

## Author

Tanmay Jain