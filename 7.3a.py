#!/usr/bin/env python

from sys import argv

result = []

with open("CAM_table.txt") as file:
    for line in file:
        words = line.split()
        if words and words[0].isdigit():
            vlan, mac, _, intf = words
            result.append([int(vlan), mac, intf])

for vlan, mac, intf in sorted(result):
    print(f"{vlan:<9}{mac:20}{intf}")