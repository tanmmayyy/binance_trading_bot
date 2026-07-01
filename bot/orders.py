from binance.exceptions import BinanceAPIException

from bot.logging_config import logger


class OrderManager:

    def __init__(self, client):

        self.client = client

    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None
    ):

        try:

            logger.info(
                f"Request : {symbol} {side} {order_type} Qty={quantity}"
            )

            if order_type == "MARKET":

                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=quantity
                )

            else:

                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="LIMIT",
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )

            logger.info(response)

            return response

        except BinanceAPIException as e:

            logger.error(e)

            raise

        except Exception as e:

            logger.error(e)

            raise