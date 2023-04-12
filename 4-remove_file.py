#!/usr/bin/env python3

import os
from sys import argv

print(f"Will remove {argv[1]}")
os.remove(argv[1])
