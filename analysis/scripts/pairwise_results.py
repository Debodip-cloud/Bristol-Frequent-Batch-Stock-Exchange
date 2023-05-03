

#static_TBSE= [('ZIC','AA',2178,16822),('ZIP','AA',6559,12441),('GDX','ZIC',10674,8326),('GDX','ZIP',8628,10372),('ZIP','ZIC',12452,6548),('GDX','AA',9401,9599),('ZIC','SHVR',4275,14725),('ZIP','SHVR',5226,13774),('AA','SHVR',10637,8363),('GDX','SHVR',15073,3927),('ZIC','GVWY',4802,14198),('ZIP','GVWY',5995,13005),('AA','GVWY',12296,6704),('GDX','GVWY',7708,11292),('GVWY','SHVR',7817,11183)]
#static_BFSE = [('AA', 'GVWY', 1860, 17140), ('AA', 'SHVR', 9379, 9621), ('GDX', 'AA', 12032, 6968), ('GDX', 'GVWY', 3174, 15826), ('GDX', 'SHVR', 9258, 9742), ('GDX', 'ZIC', 17709, 1291), ('GDX', 'ZIP', 5923, 13077), ('GVWY', 'SHVR', 10104, 8896), ('ZIC', 'AA', 5601, 13399), ('ZIC', 'GVWY', 4, 18996), ('ZIC', 'SHVR', 841, 18159), ('ZIP', 'AA', 14847, 4153), ('ZIP', 'GVWY', 7760, 11240), ('ZIP', 'SHVR', 10906, 8094), ('ZIP', 'ZIC', 18984, 16)]

#dynamic_BFBSE = [('ZIC','AA',2724,16276),('ZIP','AA',9769,9231),('GDX','ZIC',8650,10350),('GDX','ZIP',5007,13993),('ZIP','ZIC',17025,1975),('GDX','AA',10303,8697),('ZIC','SHVR',4713,14287),('ZIP','SHVR',10283,8717),('AA','SHVR',11779,7221),('GDX','SHVR',16375,2625),('ZIC','GVWY',5999,13001),('ZIP','GVWY',9165,9835),('AA','GVWY',10227,8773),('GDX','GVWY',5462,13538),('GVWY','SHVR',8430,10570)]
#static_BFBSE = [('AA', 'GVWY', 2096, 16904), ('AA', 'SHVR', 12105, 6895), ('GDX', 'AA', 12147, 6853), ('GDX', 'GVWY', 669, 18331), ('GDX', 'SHVR', 8312, 10688), ('GDX', 'ZIC', 16321, 2679), ('GDX', 'ZIP', 1518, 17482), ('GVWY', 'SHVR', 11864, 7136), ('ZIC', 'AA', 6375, 12625), ('ZIC', 'GVWY', 3, 18997), ('ZIC', 'SHVR', 918, 18082), ('ZIP', 'AA', 13503, 5497), ('ZIP', 'GVWY', 8220, 10780), ('ZIP', 'SHVR', 12312, 6688), ('ZIP', 'ZIC', 18965, 35)]


data = [('ZIC','AA',2724,16276),('ZIP','AA',9769,9231),('GDX','ZIC',8650,10350),('GDX','ZIP',5007,13993),('ZIP','ZIC',17025,1975),('GDX','AA',10303,8697),('ZIC','SHVR',4713,14287),('ZIP','SHVR',10283,8717),('AA','SHVR',11779,7221),('GDX','SHVR',16375,2625),('ZIC','GVWY',5999,13001),('ZIP','GVWY',9165,9835),('AA','GVWY',10227,8773),('GDX','GVWY',5462,13538),('GVWY','SHVR',8430,10570)]


wins = {'AA': 0, 'GVWY': 0, 'SHVR': 0, 'GDX': 0, 'ZIC': 0, 'ZIP': 0}
beats = {'AA': 0, 'GVWY': 0, 'SHVR': 0, 'GDX': 0, 'ZIC': 0, 'ZIP': 0}
dominates = {'AA': [], 'GVWY': [], 'SHVR': [], 'GDX': [], 'ZIC':[], 'ZIP': []}

for d in data:
    wins[d[0]] += d[2]
    wins[d[1]] += d[3]
    
    if d[2] > d[3]:
        beats[d[0]] += 1
        dominates[d[0]]+=[d[1]]
    else:
        beats[d[1]] += 1
        dominates[d[1]]+=[d[0]]




wins = dict(sorted(wins.items(), key=lambda x: x[1], reverse=True))
beats = dict(sorted(beats.items(), key=lambda x: x[1], reverse=True))

# Print the results
print("\n")
print('Total number of wins for each trading algorithm:')
print(wins)
print('\nNumber of algorithms beaten by each trading algorithm:')
print(beats)
print('\nNumber of algorithms dominated by each trading algorithm:')
print(dominates)
