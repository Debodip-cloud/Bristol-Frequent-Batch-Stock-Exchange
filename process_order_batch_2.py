def process_order_batch(self, time, orders, verbose):
    """
    receive a batch of orders and execute a frequent batch auction to match buyers and sellers
    :param time: Current time
    :param orders: List of orders being processed
    :param verbose: Should verbose logging be printed to the console
    :return: list of transaction records
    """




    #will need mechanism to check if all old bids have been used up
    old_asks = self.asks.lob
    old_bids = self.bids.lob

    # Partition orders into bids and asks
    new_bids = [o for o in orders if o.otype == 'Bid']
    new_asks = [o for o in orders if o.otype == 'Ask']

    asks = new_asks+old_asks
    bids = new_bids+old_bids
    
    # Initialize transaction records list
    transaction_records = []

    while bids and asks:
        # Sort bids and asks by price, with highest bids and lowest asks first
        bids.sort(key=lambda o: -o.price)
        asks.sort(key=lambda o: o.price)

        # #int returns 1 if true otherwise 0
        # #assigns best priority to items in old_orders
        # bids.sort(key=lambda o: (-o.price,int(o not in old_bids)))
        # asks.sort(key=lambda o: (o.price,int(o not in old_asks)))


        # Determine the auction price as the midpoint between the highest bid and lowest ask
        # WILL PROBABLY NEED TO CHANGE THIS TO FIND BETTER PRICE
        auction_price = (bids[0].price + asks[0].price) / 2

        # Match buyers and sellers with orders at or above the auction price
        buyers = [b for b in bids if b.price >= auction_price]
        sellers = [s for s in asks if s.price <= auction_price]

        # Sort buyers and sellers by time priority, with earliest orders first 
        # DO I NEED TO GO THROUGH ALL ORDERS OR JUST NEW ORDERS
        buyers.sort(key=lambda b: b.time)
        sellers.sort(key=lambda s: s.time)

        # Execute trades between buyers and sellers, up to the quantity available at the auction price
        trade_qty = min(sum([b.qty for b in buyers]), sum([s.qty for s in sellers]))
        while buyers and sellers and trade_qty > 0:
            buyer = buyers[0]
            seller = sellers[0]
            trade_qty = min(trade_qty, min(buyer.qty, seller.qty))
            transaction_record = {
                'type': 'Trade',
                't': time,
                'price': auction_price,
                'party1': seller.tid,
                'party2': buyer.tid,
                'qty': trade_qty,
                'coid': buyer.coid,
                'counter': seller.coid
            }
            transaction_records.append(transaction_record)
            if verbose:
                print(f'>>>>>>>>>>>>>>>>>TRADE t={time:5.2f} ${auction_price} {seller.tid} {buyer.tid}')
            buyer.qty -= trade_qty
            seller.qty -= trade_qty
            if buyer.qty == 0:
                bids.remove(buyer)
                buyers.remove(buyer)
            if seller.qty == 0:
                asks.remove(seller)
                sellers.remove(seller)

    # Add any remaining unmatched bids and asks to the order book
    for o in bids + asks:
        toid, response = self.add_order(o, verbose)
        o.toid = toid
        if verbose:
            print(f'TOID: order.toid={o.toid}')
            print(f'RESPONSE: {response}')

    # Publish the updated order book
    lob = self.publish_lob(time, False)

    return transaction_records,lob
