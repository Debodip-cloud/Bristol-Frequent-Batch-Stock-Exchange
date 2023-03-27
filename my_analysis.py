

import re
import os
import csv


if __name__ == "__main__":

    folder_path = "results"

    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path) as csvfile: # CHANGED FROM with open(file_path, newline='') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',')
                # for row in csv_reader:
                #     print(row)
                # Get the number of rows in the CSV file
                
                pattern = r'(\d+)-(\d+)-(\d+)-(\d+)-(\d+)-(\d+)'
                match = re.match(pattern,filename)
                num_traders = [int(x) for x in match.groups()]
                all_traders = ["ZIC","ZIP","GDX","AA","GVWY","SHVR"]
                trader_names = [trader for trader, num in zip(all_traders, num_traders) if num != 0]
                num_simulations = len(trader_names)

                trader_profit = [0] * len(trader_names)
                trader_trades = [0] * len(trader_names)
                
                #trader_percentage = [100* trader/sum([i for i in num_traders]) for trader in num_traders]
    
                #print(f"in file {filename} there are {num_simulations} rows and {num_traders[0]} ZIC traders which makes up {trader_percentage[0]} percent")
                
                # Iterate over the rows of the CSV file to extract the total profit of each trader and create a table with market share
                for row in csv_reader:
                    trial_id = row[0]
                    for i, trader_name in enumerate(trader_names):
                        trader_profit[i] += float(row[1+i*7+1])
                        trader_trades[i] += float(row[1+i*7+4])                    
                    
                        
                # Print the total profit and market share for each trader
                print("Trader\tProfit\tMarket Share")
                for i, trader_name in enumerate(trader_names):
                    profit = trader_profit[i]
                    #market_share = 100 * num_traders[i] * profit / sum(trader_profit)
                    trader_index = all_traders.index(trader_name)
                    trader_count = num_traders[trader_index]
                    market_share = 100*num_traders[trader_index] / sum([i for i in num_traders])
                    #market_share = trader_percentage[i]
                    print(f"{trader_name}\t{profit}\t{market_share:.2f}%")


