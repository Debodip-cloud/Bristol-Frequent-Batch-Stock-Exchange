data = [('AA', 'GVWY', 268, 18732), ('AA', 'SHVR', 9169, 9831), ('GDX', 'AA', 12099, 6901), ('GDX', 'GVWY', 149, 18851), ('GDX', 'SHVR', 6628, 12372), ('GDX', 'ZIC', 14905, 4095), ('GDX', 'ZIP', 1127, 17873), ('GVWY', 'SHVR', 18081, 919), ('ZIC', 'AA', 5615, 13385), ('ZIC', 'GVWY', 0, 19000), ('ZIC', 'SHVR', 1435, 17565), ('ZIP', 'AA', 17512, 1488), ('ZIP', 'GVWY', 838, 18162), ('ZIP', 'SHVR', 12334, 6666), ('ZIP', 'ZIC', 18846, 154)]

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
