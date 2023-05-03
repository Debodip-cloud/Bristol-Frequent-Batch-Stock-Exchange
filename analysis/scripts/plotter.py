import matplotlib.pyplot as plt


supply = [(2.00, 20), (2.50, 30), (3.00, 40), (3.50, 50), (4.00, 60), (4.50, 70), (5.00, 80)]
demand = [(5.00, 20), (4.50, 30), (4.00, 40), (3.50, 50), (3.00, 60), (2.50, 70), (2.00, 80)]





supply_price, supply_quantity = zip(*supply)
demand_price, demand_quantity = zip(*demand)


plt.plot(supply_quantity, supply_price, label='Supply')
plt.plot(demand_quantity, demand_price, label='Demand')
plt.plot([50,50],[2,3.5],color='gray',linestyle='--')
plt.plot([20,50],[3.5,3.5],color='gray',linestyle='--')


plt.scatter(50, 3.5, color='black', marker='o')
plt.text(52, 3.5, 'Equilibrium Price', ha='left', va='center', fontsize=8)



ax = plt.gca()
ax.set_xticks([])
ax.set_yticks([])
x_axis = ax.xaxis

x_axis.set_label_coords(1.05, -0.05)

y_axis = ax.yaxis
y_label = y_axis.get_label()
y_label.set_rotation(0)

y_axis.set_label_coords(-0.05, 1.00)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.xlabel('Quantity')
plt.ylabel('Price')
##plt.title('Supply and Demand Curves')
plt.legend()
plt.show()

plt.savefig("EQ.jpg")


plt.show()
