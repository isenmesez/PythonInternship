#!/usr/bin/env python

from sys import argv

with open("CAM_table.txt") as file:
    for line in file:
        words = line.split()
        if words and words[0].isdigit():
            vlan, mac, _, interface = words
            print(f"{vlan:9}{mac:20}{interface}")