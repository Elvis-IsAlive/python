#! /usr/bin/python3.7

import random

heads = 0
for i in range(1000):
    if random.randint(0,1) == 1:
        heads += 1
    if i == 500:
        print("halfway")
print("heads: " + str(heads))
