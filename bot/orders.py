 try:
        logger.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

        if order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
        else:
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )

        logger.info(f"Order response: {order}")
        return order

    except Exception as e:
        logger.error(f"Error placing order: {e}")
        raise
