data = [('AA', 'SHVR', 7451, 11549), ('GDX', 'AA', 11775, 7225), ('GDX', 'GVWY', 419, 18581), ('GDX', 'SHVR', 6691, 12309), ('GDX', 'ZIC', 17033, 1967), ('GDX', 'ZIP', 2521, 16479), ('GVWY', 'SHVR', 17230, 1770), ('ZIC', 'AA', 4858, 14142), ('ZIC', 'GVWY', 0, 19000), ('ZIC', 'SHVR', 1097, 17903), ('ZIP', 'AA', 17065, 1935), ('ZIP', 'GVWY', 943, 18057), ('ZIP', 'SHVR', 10451, 8549), ('ZIP', 'ZIC', 18738, 262)]
# Create a dictionary to store the total number of wins for each trading algorithm
wins = {'AA': 0, 'GVWY': 0, 'SHVR': 0, 'GDX': 0, 'ZIC': 0, 'ZIP': 0}
# Create a dictionary to store the number of algorithms beaten by each trading algorithm
beats = {'AA': 0, 'GVWY': 0, 'SHVR': 0, 'GDX': 0, 'ZIC': 0, 'ZIP': 0}

# Loop through the data and update the wins dictionary
for d in data:
    wins[d[0]] += d[2]
    wins[d[1]] += d[3]
    
    if d[2] > d[3]:
        beats[d[0]] += 1
    else:
        beats[d[1]] += 1


wins = dict(sorted(wins.items(), key=lambda x: x[1], reverse=True))
beats = dict(sorted(beats.items(), key=lambda x: x[1], reverse=True))

# Print the results
print('Total number of wins for each trading algorithm:')
print(wins)
print('\nNumber of algorithms beaten by each trading algorithm:')
print(beats)
