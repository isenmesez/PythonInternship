#!/usr/bin/env python

from sys import argv

ignore = ["duplex", "alias", "configuration"]
file1 = argv[1]
file2 = argv[2]
file = ''.join(file1)
with open(file1) as file1, open(file2, 'w') as file2:
    for line in file1:
        words = line.split()
        check = set(words) & set(ignore)
        if not line.startswith("!") and not check:
            file2.write(line)