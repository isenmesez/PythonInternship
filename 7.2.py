#!/usr/bin/env python

from sys import argv

file = argv[1:]
file = ''.join(file)
with open(file, 'r') as file:
    for line in file:
        if line.find('!') == -1:
            print(line.strip('\n'))
