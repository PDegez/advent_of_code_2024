# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 10:45:36 2024

@author: pauli
"""

from collections import Counter

with open("./d1_input.txt", "r", encoding="UTF8") as file:
    l1 = []
    l2 = []
    for line in file.readlines():
        pair = line.split("   ")
        l1.append(int(pair[0].strip()))
        l2.append(int(pair[1].strip()))

l1s = sorted(l1)
l2s = sorted(l2)

distance = 0
for i in range(len(l1s)):
    distance += abs(l1s[i]-l2s[i])

print(f"distance = {distance}")

similarity = 0
countl1 = Counter(l1)
countl2 = Counter(l2)

for key, value in Counter(l1).items():
    similarity += countl2.get(key, 0)*key

print(f"similarity = {similarity}")