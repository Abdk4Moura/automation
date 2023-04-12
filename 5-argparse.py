#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(
    description="Just something to test the sweetness of the argparse module"
)
parser.add_argument("-p", "--position", type=int)
parser.add_argument("-s", "--sample", type=int)

args = parser.parse_args()
col = args.position
sample = args.sample

print(col)
print(sample)
