from tbse_sys_consts import TICK_SIZE

def process_order_batch(self, time, orders, verbose):
    """
    receive a batch of orders and check if crossing takes place.
    if crossing takes place, process orders and respond to traders. make sure new LOB is published
    """
    old_asks = self.asks.lob
    old_bids = self.bids.lob

    most_recent_orders = []
    for order in orders:
        [toid, response] = self.add_order(order,verbose)
        order.toid = toid
        if verbose:
            print(f'TOID: order.toid={order.toid}')
            print(f'RESPONSE: {response}')
        
        most_recent_orders.append(order)

    best_ask = self.asks.best_price 
    best_bid = self.bids.best_price 

    if best_ask>best_bid: #there is no crossing, publish up-to-date LOB and there are no transaction records
        lob = self.publish_lob(time, False)
        return None,lob
    
    demand_curve,supply_curve = self.construct_curves()
    equilibrium_price,rationing = find_equilibrium(demand_curve,supply_curve)
    
    transaction_records = []
    
    #There is no need for rationing in the case of a vertical intersection where p* is the midpoint.
    if rationing==False: #sort orders by price to determine where to ration from
    #go through old orders or just new orders or both?? 
    #equlibrium might have changed so need to go through all orders. for rationing go through list of orders 
        for order in orders:
            counterparty = None
            counter_coid = None
    
            if order.otype == 'Bid' and order.price > equilibrium_price:
                if self.asks.n_orders > 0:
                    for old_order in old_asks: #
                        if old_order.price<equilibrium_price:
                            counterparty = old_order.tid
                            counter_coid = old_order.coid

                    counterparty = old_order.tid
                    counter_coid = self.asks.orders[counterparty].coid

                    self.asks.delete_order(time,old_order)
                    self.bids.delete_order(time,order)

                    if counterparty is not None:
                        # process the trade
                        if verbose:
                            print(f'>>>>>>>>>>>>>>>>>TRADE t={time:5.2f} ${equilibrium_price} {counterparty} {order.tid}')
                        transaction_record = {
                            'type': 'Trade',
                            't': time,
                            'price': price,
                            'party1': counterparty,
                            'party2': order.tid,
                            'qty': order.qty,
                            'coid': order.coid,
                            'counter': counter_coid
                        }
                        self.tape.append(transaction_record)    
                        transaction_records.append(transaction_record) 
                    
                    if verbose:
                        print('counterparty, price', counterparty, equilibrium_price)

            elif order.otype == 'Ask' and order.price < equilibrium_price:
                if self.bids.n_orders > 0:
                    #find matching order to uncross with from old list.
                    for old_order in old_bids:
                        if old_order.price>equilibrium_price:
                            counterparty = old_order.tid
                            counter_coid = old_order.coid

                    counterparty = old_order.tid
                    counter_coid = self.bids.orders[counterparty].coid
                    
                    self.asks.delete_order(time,old_order)
                    self.bids.delete_order(order)

                    if counterparty is not None:
                        # process the trade
                        if verbose:
                            print(f'>>>>>>>>>>>>>>>>>TRADE t={time:5.2f} ${price} {counterparty} {order.tid}')
                        transaction_record = {
                            'type': 'Trade',
                            't': time,
                            'price': price,
                            'party1': counterparty,
                            'party2': order.tid,
                            'qty': order.qty,
                            'coid': order.coid,
                            'counter': counter_coid
                        }
                        self.tape.append(transaction_record)     
                    
                    if verbose:
                        print('counterparty, price', counterparty, equilibrium_price)
            else:
                # we should never get here
                sys.exit('process_order() given neither Bid nor Ask')
            # NB at this point we have deleted the order from the exchange's records
            # but the two traders concerned still have to be notified
            if verbose:
                print(f'counterparty {counterparty}')

    lob = self.publish_lob(time, False)
    return transaction_records,lob
    #can I return whole tape and be ok or do I have to return single transactions   
    #return transaction_record, lob #make sure no transaction is returned if nothing happens
    # return self.tape, lob #return whole tape and process transactions

def construct_curves(self):
    #CONSTRUCT SUPPLY AND DEMAND HERE AND GET p* and q* so crossing can take place. reverse LOB so it is a function of quantity
    demand_curve = {} 
    demand_quantity = 0
    for i in range(0,self.bids.lob_depth):
        #price,quantity = self.bids.lob_anon[0],self.bids.lob_anon[1]
        price,quantity = self.bids.lob_anon[i]
        demand_quantity+=quantity
        demand_curve[price] = demand_quantity

    supply_curve ={}
    supply_quantity = 0
    for i in range(0,self.asks.lob_depth):
        #price,quantity = self.asks.lob_anon[0],self.asks.lob_anon[1]
        price,quantity = self.asks.lob_anon[i]
        supply_quantity+=quantity
        supply_curve[price] = supply_quantity


    #populate curves with duplicate values in crossing range so we get stepped curves not just points
    for price in range(best_ask,best_bid,TICK_SIZE):
        if price not in supply_curve:
            #supply_curve[price] = min([q for p,q in supply_curve.keys() if p> price])
            supply_curve[price] = min([q for p,q in supply_curve.items() if p> price])

        if price not in demand_curve:
            demand_curve[price] = max([q for p,q in demand_curve.items() if p< price])
    
    return demand_curve,supply_curve

def find_equilibrium(self,,demand_curve,supply_curve):
     #find equilibrium
    equilibrium_prices = []
    #equilibrium_quantity = 0 #do I need this?
    rationing = True
    
    for price in range(best_ask,best_bid,TICK_SIZE):
        if(demand_curve[price]==supply_curve[price]):
            equilibrium_prices.append(price)
            #equilibrium_quantity = demand_curve[price]
    
    #knife edge case e case in which supply and demand intersect vertically instead of horizontally
    if len(equilibrium_prices)>1: #not necessarily true. change this.
        equilibrium_price = equilibrium_price[0]+0.5*(equilibrium_price[0]-equilibrium_price[-1])
        rationing=False #or true 
    else:
        equilibrium_price = equilibrium_prices[-1]

    return equilibrium_price,rationing  

