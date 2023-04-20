#!/usr/bin/env python3

from os import path

novel_exists: bool = path.exists("novel.txt")

another_thing_exists: bool = path.exists("another_thing.txt")

if novel_exists:
    print("file `novel.txt` exists")

if another_thing_exists:
    print("file `another_thing.txt` exists")
