import matplotlib.pyplot as plt

supply = [(440, 10), (412, 9), (403, 8), (382, 7), (304, 6), (131.0, 5), (98.0, 4), (75.0, 3), (64.0, 2), (53.0, 1)]

demand = [(143.0, 1), (98, 2), (85, 3), (75.0, 4), (64.0, 5), (63, 6), (56, 7), (53.0, 8), (42.0, 9), (27, 10)]

supply_price, supply_quantity = zip(*supply)
demand_price, demand_quantity = zip(*demand)

plt.plot(supply_quantity, supply_price, label='Supply')
plt.plot(demand_quantity, demand_price, label='Demand')

plt.xlabel('Quantity')
plt.ylabel('Price')
plt.title('Supply and Demand Curves')

plt.legend()

plt.show()
