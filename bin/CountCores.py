#!/usr/bin/env python
file = tuple(open('/proc/cpuinfo', 'r'))
cores = 0
TotalCores = 0
for line in file:
    if 'cpu cores' in line:
        cores = line.split()[-1]
        TotalCores += int(cores)
print TotalCores
