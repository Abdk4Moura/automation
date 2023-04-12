#!/usr/bin/env python3
#
# There's a limited number of file descriptors that can be created until the system
# before the os runs out of them

file = open("txt/spider.txt")

## this `file` variable is open for test in an Ipython console
## continuously using the readline method of the file descriptor until
## the buffer is completely consumed will thereafter make the file.readline()
## return a `''`.

# you can also use print with `read` or `readline``

file.close()
