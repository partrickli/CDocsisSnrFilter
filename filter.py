#!/usr/bin/env python

# serial number collect
lines = [l for l in open("./serialNumber")]


def serialNumberOf(line):
  words = line.split()
  nodeIndex = int(words[2].strip())
  serialNumber = words[-1].strip()
  return (nodeIndex, serialNumber)


serialDict = {}
for l in lines:
  nodeIndex, serialNumber = serialNumberOf(l)
  serialDict[nodeIndex] = serialNumber

for key in serialDict:
  print("{}: {}".format(key, serialDict[key]))
