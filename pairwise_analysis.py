import os
import csv

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


def process_csv_file(file_name):
    trader1_wins = 0
    trader2_wins = 0
    trader1_count = 0
    with open(file_name, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            trader1_count = int(row[3])
            trader1_profit = float(row[4])
            trader2_profit = float(row[11])
            if trader1_profit > trader2_profit:
                trader1_wins += 1
            elif trader1_profit < trader2_profit:
                trader2_wins += 1
    trader1_count/=2
    return [trader1_count,trader1_wins, trader2_wins]


def process_csv_folder(folder_path):
    # trader_names = ["ZIP", "ZIC", "GDX", "AA", "GVWY", "SHVR"]
    total_wins = [0, 0]
    all_wins = {}
    trader1_wins = 0
    trader2_wins = 0
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv"):
            trader1_count, trader1_wins, trader2_wins = process_csv_file(os.path.join(folder_path, file_name))
            
            all_wins[trader1_count] = [trader1_wins, trader2_wins]

            total_wins[0] += trader1_wins
            total_wins[1] += trader2_wins
    
    sorted_all_wins = dict(sorted(all_wins.items()))

    return sorted_all_wins, total_wins



folder_path = "results/ZIPvsZIC"
folder_wins = process_csv_folder(folder_path)

print(folder_wins)
