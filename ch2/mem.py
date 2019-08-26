#! /usr/bin/env python3

from os import getpid
from sys import argv
from time import time

pid = getpid()
x = int(argv[1])

def delay(sec):
    waitUntil = time() + sec
    while (time() < waitUntil):
        pass

while True:
    print("(pid=%d) x=%d" % (pid, x))
    delay(1)
    x += 1


