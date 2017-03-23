import numpy as np
import io
import sys
try: 
    from pyne.data import atomic_mass
except:
    print('some weird import bug in pyne that makes the first import fail')
from pyne.data import atomic_mass
lines = sys.stdin.readlines()
w = open('out.txt', 'w')
inventory = {}
for line in lines:
    line = line.split(' ')
    if line[0] == 'time':
        del(line[0])
        time = np.asarray(line)
        time.astype(np.float)
    elif line[0] == 'Inv':
        del(line[0])
        iso = line[0]+line[1]
        iso = int(float(iso))
        del(line[0:3])
        del(line[-1])
        values = np.asarray(line)
        values = values.astype(np.float) 
        inventory[iso] = values
    else:
        continue
total = 0.0
for iso in inventory:
    total += inventory[iso][0] * atomic_mass(iso)
for iso in inventory:
    inventory[iso] *= atomic_mass(iso) * total
print(inventory[92238])
