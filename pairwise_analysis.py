import os
import csv
import re
import matplotlib.pyplot as plt


def get_trader_names(file_name, trader_names):
    parts = file_name.split("-")
    trader1 = None
    trader2 = None
    for i in range(1, len(parts)):
        if parts[i] == "19" or parts[i] == "19.csv":
            trader1 = trader_names[i]
        if parts[i] == "01" or parts[i] == "01.csv":
            trader2 = trader_names[i]
    return [trader1, trader2]


def process_csv_file(file_name,master_trader):
    trader1_wins = 0
    trader2_wins = 0
    trader1_count = 0
    with open(file_name, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            trader1_profit = float(row[4])
            trader2_profit = float(row[11])
            if trader1_profit >= trader2_profit:
                trader1_wins += 1
            elif trader1_profit < trader2_profit:
                trader2_wins += 1
    trader1_count/=2


    with open(file_name, newline="") as f:
        reader = csv.reader(f)
        first_row = next(reader)

    trader1_name = first_row[1][1:]
    trader1_count = int(first_row[3])
    trader2_count = int(first_row[10])
    if trader1_name==master_trader:
        return [trader1_count,trader1_wins, trader2_wins]
    else:
        return [trader2_count,trader2_wins, trader1_wins]
    


def process_csv_folder(folder_path):

    match = re.search(r'/(?P<trader1>\w+)vs', folder_path)
    master_trader = match.group('trader1')
    total_wins = [0, 0]
    all_wins = {}
    trader1_wins = 0
    trader2_wins = 0
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv"):
            trader1_count, trader1_wins, trader2_wins = process_csv_file(os.path.join(folder_path, file_name),master_trader)
            all_wins[trader1_count] = [trader1_wins, trader2_wins]
            total_wins[0] += trader1_wins
            total_wins[1] += trader2_wins
    
    sorted_all_wins = dict(sorted(all_wins.items()))


    comparison = re.search(r'results\/(.+)', folder_path).group(1)
    # Calculate the difference in wins for each trader
    win_diffs = {k: v[0] - v[1] for k, v in sorted_all_wins.items()}

    # Plot the trader number (key) against the win difference (value)
    plt.bar(win_diffs.keys(), win_diffs.values())
    plt.xlabel("Trader")
    plt.ylabel("Wins Difference")
    plt.title("Trader Wins Difference")
    plt.savefig(comparison.pdf)
    plt.show()

    return sorted_all_wins, total_wins


folder_path = "results/GDXvsZIC"
all_wins, total_wins = process_csv_folder(folder_path)
print(all_wins)
