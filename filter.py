#!/usr/bin/env python

 serial part # serial number collect
 serial part lines = [l for l in open("./serialNumber")]
 serial part 
 serial part 
 serial part def serialNumberOf(line):
 serial part   words = line.split()
 serial part   nodeIndex = int(words[2].strip())
 serial part   serialNumber = words[-1].strip()
 serial part   return (nodeIndex, serialNumber)
 serial part 
 serial part 
 serial part serialDict = {}
 serial part for l in lines:
 serial part   nodeIndex, serialNumber = serialNumberOf(l)
 serial part   serialDict[nodeIndex] = serialNumber
 serial part 
 serial part for key in serialDict:
 serial part   print("{}: {}".format(key, serialDict[key]))
