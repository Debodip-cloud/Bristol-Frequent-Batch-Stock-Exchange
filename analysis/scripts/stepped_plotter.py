import matplotlib.pyplot as plt
import numpy as np


def find_equilibrium_price(supply, demand):
        # Initialize variables to store the best price and the smallest net surplus
        best_prices = [-1]
        smallest_net_surplus = 1000

        # Loop over the prices in the demand curve and find the best price
        for price, demand_qty in demand: #could step through all prices and make p* halfway point between valid prices
            # Find the quantity of the good supplied at the current price
            suppliers = [(x[0],x[1]) for x in supply if price>=x[0]]
            
            if suppliers == []:
                break
            else:
                #get best ask price at given price in bids 
                supply_price,supply_qty = suppliers[0]     
        
            
            # Calculate the consumer surplus and producer surplus at the current price
            consumer_surplus = demand_qty
            producer_surplus = supply_qty
            
            net_surplus = abs(consumer_surplus - producer_surplus)

            if net_surplus<smallest_net_surplus:
                #best_price = supply_price
                best_prices=[supply_price]
                smallest_net_surplus = net_surplus
            elif net_surplus==smallest_net_surplus:
                best_prices.append(supply_price)
                smallest_net_surplus = net_surplus

        if len(best_prices)==1:
            best_price = best_prices[0]
        else:
            best_price= sum(best_prices) / len(best_prices)
        
        return best_price

def find_equilibrium_price_new1(supply, demand):
    # Initialize variables to store the best prices and the smallest net surplus
    best_supply_prices = [-1]
    best_demand_prices = [-1]
    smallest_net_surplus = 1000

    # Loop over the prices in the demand curve and find the best prices
    for demand_price, demand_qty in demand:
        # Find the quantity of the good supplied at the current price
        suppliers = [(supply_price, supply_qty) for supply_price, supply_qty in supply if supply_price <= demand_price]

        if not suppliers:
            break

        # Get the best ask price at the given demand price in the bids
        supply_price, supply_qty = max(suppliers, key=lambda x: x[0])

        # Calculate the consumer surplus and producer surplus at the current price
        consumer_surplus = demand_qty
        producer_surplus = supply_qty

        net_surplus = abs(consumer_surplus - producer_surplus)

        if net_surplus < smallest_net_surplus:
            best_supply_prices = [supply_price]
            best_demand_prices = [demand_price]
            smallest_net_surplus = net_surplus
        elif net_surplus == smallest_net_surplus:
            best_supply_prices.append(supply_price)
            best_demand_prices.append(demand_price)

    if len(best_supply_prices) == 1:
        best_supply_price = best_supply_prices[0]
    else:
        best_supply_price = sum(best_supply_prices) / len(best_supply_prices)

    if len(best_demand_prices) == 1:
        best_demand_price = best_demand_prices[0]
    else:
        best_demand_price = sum(best_demand_prices) / len(best_demand_prices)

    # Calculate the equilibrium price as the midpoint of the best supply and demand prices
    equilibrium_price = (best_supply_price + best_demand_price) / 2

    return equilibrium_price

def find_equilibrium_price_new(supply, demand):
    # Check for knife edge case
    supply_prices = set([price for price, qty in supply])
    demand_prices = set([price for price, qty in demand])
    intersect = supply_prices.intersection(demand_prices)
    if len(intersect) == 1:
        # Knife edge case: supply and demand intersect vertically
        equilibrium_price = intersect.pop()
    else:
        # Initialize variables to store the best prices and the smallest net surplus
        best_supply_prices = [-1]
        best_demand_prices = [-1]
        smallest_net_surplus = 1000

        # Loop over the prices in the demand curve and find the best prices
        for demand_price, demand_qty in demand:
            # Find the quantity of the good supplied at the current price
            suppliers = [(supply_price, supply_qty) for supply_price, supply_qty in supply if supply_price <= demand_price]

            if not suppliers:
                break

            # Get the best ask price at the given demand price in the bids
            supply_price, supply_qty = max(suppliers, key=lambda x: x[0])

            # Calculate the consumer surplus and producer surplus at the current price
            consumer_surplus = demand_qty
            producer_surplus = supply_qty

            net_surplus = abs(consumer_surplus - producer_surplus)

            if net_surplus < smallest_net_surplus:
                best_supply_prices = [supply_price]
                best_demand_prices = [demand_price]
                smallest_net_surplus = net_surplus
            elif net_surplus == smallest_net_surplus:
                best_supply_prices.append(supply_price)
                best_demand_prices.append(demand_price)

        if len(best_supply_prices) == 1:
            best_supply_price = best_supply_prices[0]
        else:
            best_supply_price = sum(best_supply_prices) / len(best_supply_prices)

        if len(best_demand_prices) == 1:
            best_demand_price = best_demand_prices[0]
        else:
            best_demand_price = sum(best_demand_prices) / len(best_demand_prices)

        # Calculate the equilibrium price as the midpoint of the best supply and demand prices
        equilibrium_price = (best_supply_price + best_demand_price) / 2

    return equilibrium_price


# demand = [(143.0, 1), (98, 2), (85, 3), (75.0, 4), (64.0, 5), (63, 6), (56, 7), (53.0, 8), (42.0, 9), (27, 10)]
# supply = [(440, 10), (412, 9), (403, 8), (382, 7), (304, 6), (131.0, 5), (98.0, 4), (75.0, 3), (64.0, 2), (53.0, 1)]
supply = [(200,2),(100,1)]
demand = [(120,1),(80,2)]
# demand = [(140, 1), (139, 2)]
# supply = [(140, 2), (135, 1)]
supply= [(128, 4), (104, 3), (85, 2), (62, 1)]
demand=[(120, 1), (74, 2), (72, 3), (58, 4)]

quantities = sorted(set([d[1] for d in demand] + [s[1] for s in supply]))

price_demanded = []
price_supplied = []

for quantity in quantities:
    price_demanded.append(max([d[0] for d in demand if d[1] >= quantity]))
    price_supplied.append(min([s[0] for s in supply if s[1] >= quantity]))

x_demand = np.repeat(quantities, 2)[1:]
y_demand = np.repeat(price_demanded, 2)[:-1]

x_supply = np.repeat(quantities, 2)[1:]
y_supply = np.repeat(price_supplied, 2)[:-1]


### EQUILIBRIUM STUFF ###

EQ = find_equilibrium_price_new(supply,demand)
print("EQ IS %d",EQ)
plt.axhline(y = EQ, color = 'g', linestyle = '--')

old_EQ = find_equilibrium_price(supply,demand)
print("old_EQ IS %d",old_EQ)
plt.axhline(y = old_EQ, color = 'r', linestyle = '--')

### EQUILIBRIUM STUFF ###

plt.step(x_demand, y_demand, label='Demand')
plt.step(x_supply, y_supply, label='Supply')
plt.xlabel('Quantity')
plt.ylabel('Price')
plt.title('Stepped Supply and Demand Curves')
# plt.xlim(0)
# plt.ylim(0, 500)
plt.legend()
plt.show()
