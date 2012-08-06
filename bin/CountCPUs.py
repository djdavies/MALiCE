#!/usr/bin/env python
file = tuple(open('/proc/cpuinfo', 'r'))
TotalCPUs = 0
for line in file:
    if 'processor' in line:
        TotalCPUs += 1
print TotalCPUs
