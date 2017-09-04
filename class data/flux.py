import io
import numpy as np
import matplotlib.pyplot as plt

#32 groups
f = open('32g.out', 'r')
lines = f.readlines()
start = lines.index(' ============================>     TALLY 3     <============================\n')
end = lines.index(' ============================>     TALLY 4     <============================\n')
bins32 = []
flux32 = []
for line in lines[start:end]:
    line = line.strip().split()
    if not line:
        continue
    elif line[0] == 'Incoming':
        bins32.append(line[-1].strip('\\\)\\\n'))
    elif line[0] == 'Flux':
        flux32.append(line[1])
    else:
        continue

#1000 groups
f = open('1000g.out', 'r')
lines = f.readlines()
start = lines.index(' ============================>     TALLY 3     <============================\n')
end = lines.index(' ============================>     TALLY 4     <============================\n')
bins1000 = []
flux1000 = []
for line in lines[start:end]:
    line = line.strip().split()
    if not line:
        continue
    elif line[0] == 'Incoming':
        bins1000.append(line[-1].strip('\\\)\\\n'))
    elif line[0] == 'Flux':
        flux1000.append(line[1])
    else:
        continue

x1 = bins32
y1 = flux32
x2 = bins1000
y2 = flux1000

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()


large = ax1.step(x2, y2, 'g-', label = 'G=1000', zorder=10)
small = ax2.step(x1, y1, 'k-', label = 'G=32', zorder=1)

ax1.set_xlabel('Energy [MeV]')
ax2.set_ylabel('Normalized Flux [n/s/cm$^2$] G=32')
ax1.set_ylabel('Normalized Flux [n/s/cm$^2$] G=1000')
ax1.set_xscale('log')
ax1.set_yscale('log')
ax2.set_xscale('log')
ax2.set_yscale('log')
lns = small + large
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=0)
plt.show()


