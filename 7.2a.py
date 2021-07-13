#!/usr/bin/env python

from sys import argv

ignore = ["duplex", "alias", "configuration"]
file = argv[1:]
file = ''.join(file)
with open(file) as file:
    for line in file:
        words = line.split()
        check = set(words) & set(ignore)
        if not line.startswith("!") and not check:
            print(line.rstrip())