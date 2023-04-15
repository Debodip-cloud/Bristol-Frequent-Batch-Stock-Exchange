import pandas as pd
import matplotlib.pyplot as plt

# Load csv file as pandas dataframe
df = pd.read_csv("test_table_summed.csv")

# Get list of unique traders
traders = df["Trader"].unique()

# Create a new figure
fig, ax = plt.subplots()

# Plot each trader's profit vs market share on the same figure
for trader in traders:
    trader_df = df[df["Trader"]==trader]
    ax.plot(trader_df["Market Share"], trader_df["Profit"], label=trader)

# Set x-axis label
ax.set_xlabel("Market Share")

# Set y-axis label
ax.set_ylabel("Profit")

# Add legend
ax.legend()

# Show the plot
plt.savefig("output_test.png")
