data = [('AA', 'GVWY', 27, 18973), ('AA', 'SHVR', 4203, 14797), ('GDX', 'AA', 17305, 1695), ('GDX', 'GVWY', 395, 18605), ('GDX', 'SHVR', 15637, 3363), ('GDX', 'ZIC', 17388, 1612), ('GDX', 'ZIP', 6108, 12892), ('GVWY', 'SHVR', 18792, 208), ('ZIC', 'AA', 4583, 14417), ('ZIC', 'GVWY', 0, 19000), ('ZIC', 'SHVR', 1955, 17045), ('ZIP', 'AA', 16420, 2580), ('ZIP', 'GVWY', 40, 18960), ('ZIP', 'SHVR', 14114, 4886), ('ZIP', 'ZIC', 18605, 395)]
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
