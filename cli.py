import argparse

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import *

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price")

args = parser.parse_args()

try:

    side = validate_side(args.side)

    order_type = validate_order_type(args.type)

    quantity = validate_quantity(args.quantity)

    if order_type == "LIMIT" and args.price is None:
        raise ValueError("Price required for LIMIT")

    client = BinanceClient().client

    manager = OrderManager(client)

    result = manager.place_order(
        args.symbol.upper(),
        side,
        order_type,
        quantity,
        args.price
    )

    print("\n========== ORDER SUMMARY ==========")

    print(f"Symbol : {args.symbol}")
    print(f"Side : {side}")
    print(f"Type : {order_type}")
    print(f"Quantity : {quantity}")

    if args.price:
        print(f"Price : {args.price}")

    print("\n========== RESPONSE ==========")

    print("Order ID :", result.get("orderId"))
    print("Status :", result.get("status"))
    print("Executed Qty :", result.get("executedQty"))
    print("Avg Price :", result.get("avgPrice"))

    print("\nSUCCESS")

except Exception as e:

    print("FAILED")

    print(e)