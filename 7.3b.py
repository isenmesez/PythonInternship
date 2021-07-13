#!/usr/bin/env python

from sys import argv

vlan_number = input("Enter VLAN number: ")

with open("CAM_table.txt") as file:
    for line in file:
        words = line.split()
        if words and words[0].isdigit() and words[0] == vlan_number:
            vlan, mac, _, intf = words
            print(f"{vlan:9}{mac:20}{intf}")