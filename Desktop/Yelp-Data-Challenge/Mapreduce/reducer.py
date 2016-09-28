#!/usr/bin/python
import sys
attire = None
Count = [0]*24
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
# Something has gone wrong. Skip this line.
        continue
    thisCity, thisattire = data_mapped
    if oldCity and oldCity != thisCity:
        max_value = max(thisattire)
        max_index = thisattire.index(max_value)
        print oldCity, max_index
        oldCity = thisCity
    Count = [0]*24
    oldCity = thisCity
    Count[int(attire)] += 1
