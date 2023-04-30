#data = [('AA', 'GVWY', 1860, 17140), ('AA', 'SHVR', 9379, 9621), ('GDX', 'AA', 12032, 6968), ('GDX', 'GVWY', 3174, 15826), ('GDX', 'SHVR', 9258, 9742), ('GDX', 'ZIC', 17709, 1291), ('GDX', 'ZIP', 5923, 13077), ('GVWY', 'SHVR', 10104, 8896), ('ZIC', 'AA', 5601, 13399), ('ZIC', 'GVWY', 4, 18996), ('ZIC', 'SHVR', 841, 18159), ('ZIP', 'AA', 14847, 4153), ('ZIP', 'GVWY', 7760, 11240), ('ZIP', 'SHVR', 10906, 8094), ('ZIP', 'ZIC', 18984, 16)]
data = [('AA', 'GVWY', 2096, 16904), ('AA', 'SHVR', 12105, 6895), ('GDX', 'AA', 12147, 6853), ('GDX', 'GVWY', 669, 18331), ('GDX', 'SHVR', 8312, 10688), ('GDX', 'ZIC', 16321, 2679), ('GDX', 'ZIP', 1518, 17482), ('GVWY', 'SHVR', 11864, 7136), ('ZIC', 'AA', 6375, 12625), ('ZIC', 'GVWY', 3, 18997), ('ZIC', 'SHVR', 918, 18082), ('ZIP', 'AA', 13503, 5497), ('ZIP', 'GVWY', 8220, 10780), ('ZIP', 'SHVR', 12312, 6688), ('ZIP', 'ZIC', 18965, 
35)]
wins = {'AA': 0, 'GVWY': 0, 'SHVR': 0, 'GDX': 0, 'ZIC': 0, 'ZIP': 0}
beats = {'AA': 0, 'GVWY': 0, 'SHVR': 0, 'GDX': 0, 'ZIC': 0, 'ZIP': 0}

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
