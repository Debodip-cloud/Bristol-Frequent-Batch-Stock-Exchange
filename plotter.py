import matplotlib.pyplot as plt

supply = [(440, 10), (412, 9), (403, 8), (382, 7), (304, 6), (131.0, 5), (98.0, 4), (75.0, 3), (64.0, 2), (53.0, 1)]

demand = [(143.0, 1), (98, 2), (85, 3), (75.0, 4), (64.0, 5), (63, 6), (56, 7), (53.0, 8), (42.0, 9), (27, 10)]


supply = [(100,1),(200,2)]

demand = [(120,1),(80,2)]



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


def find_equilibrium_price_new(supply_curve, demand_curve):
    """
    Finds the equilibrium price from a supply curve and a demand curve.

    supply_curve: a list of tuples, where each tuple is of the form (price, quantity) representing the quantity supplied at a given price.
    demand_curve: a list of tuples, where each tuple is of the form (price, quantity) representing the quantity demanded at a given price.

    Returns the equilibrium price, or None if there is no equilibrium.
    """
    # Initialize variables
    total_quantity_supplied = sum(q for p, q in supply_curve)
    total_quantity_demanded = sum(q for p, q in demand_curve)
    excess_demand = total_quantity_demanded - total_quantity_supplied
    excess_supply = total_quantity_supplied - total_quantity_demanded
    equilibrium_price = None

    # Case 1: excess demand
    if excess_demand > 0:
        demand_curve.sort(reverse=True)  # sort demand curve in descending order of price
        for demand_price, demand_quantity in demand_curve:
            cumulative_quantity = 0
            for supply_price, supply_quantity in supply_curve:
                if supply_price <= demand_price:
                    cumulative_quantity += supply_quantity
                else:
                    break
            if demand_quantity <= cumulative_quantity:
                equilibrium_price = demand_price
                break

    # Case 2: excess supply
    elif excess_supply > 0:
        supply_curve.sort()  # sort supply curve in ascending order of price
        for supply_price, supply_quantity in supply_curve:
            cumulative_quantity = 0
            for demand_price, demand_quantity in demand_curve:
                if demand_price >= supply_price:
                    cumulative_quantity += demand_quantity
                else:
                    break
            if supply_quantity <= cumulative_quantity:
                equilibrium_price = supply_price
                break

    # Case 3: equilibrium
    else:
        demand_curve.sort(reverse=True)  # sort demand curve in descending order of price
        for demand_price, demand_quantity in demand_curve:
            if demand_quantity <= excess_supply:
                equilibrium_price = demand_price
                break
            excess_supply += demand_quantity
        if equilibrium_price is None:
            supply_curve.sort()  # sort supply curve in ascending order of price
            for supply_price, supply_quantity in supply_curve:
                if supply_quantity <= excess_demand:
                    equilibrium_price = supply_price
                    break
                excess_demand += supply_quantity

    return equilibrium_price


supply_price, supply_quantity = zip(*supply)
demand_price, demand_quantity = zip(*demand)



# EQ = find_equilibrium_price_new(supply,demand)
# old_EQ = find_equilibrium_price(supply,demand)
# plt.plot(supply_quantity, supply_price, label='Supply')
# plt.plot(demand_quantity, demand_price, label='Demand')
# print("EQ IS %d",EQ)
# print("old_EQ IS %d",old_EQ)
# plt.axhline(y = EQ, color = 'r', linestyle = '-')
# plt.axhline(y = old_EQ, color = 'r', linestyle = '-')
# plt.xlabel('Quantity')
# plt.ylabel('Price')
# plt.title('Supply and Demand Curves')

plt.legend()

plt.show()
