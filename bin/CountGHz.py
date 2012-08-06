#!/usr/bin/env python
file = tuple(open('/proc/cpuinfo', 'r'))
MHz = 0.0
cores = 0
TotalCores = 0
TotalMHz = 0.0
for line in file:
    if 'cpu MHz' in line:
        MHz = line.split()[-1]
    if 'cpu cores' in line:
        cores = line.split()[-1]
        TotalCores += int(cores)
        TotalMHz += (float(MHz) * float(cores))
print int(TotalMHz / 1024.0)
