#!/usr/bin/env python

def snrRelated(l):
  if "I/F" in l or "MER(dB)" in l:
    return True

def merOf(line):
  merString = line.split(":")[1]
  mer = float(merString.strip())
  return mer
  

def nodeIndexOf(line):
  print(line)
  interfaceString = line.split(":")[1].strip()
  print(interfaceString)
  nodeIndex = int(interfaceString.split("/")[0])
  return nodeIndex


# main

lines = [l for l in open("./signal")]
lineCount = len(lines)

filtered = [l.strip() for l in lines if snrRelated(l)]

nodeStrings = []
for i in range(len(filtered)/2):
  node = {}
  node["interfaceString"] = filtered[i * 2]
  node["merString"] = filtered[i * 2 + 1]
  nodeStrings.append(node)

for node in nodeStrings:
  print("--------node--------")
  for k in node:
    print("{} ##### {}".format(k, node[k]))


#snrDict = {}
#
#for node in nodeStrings[1:2]:
#  nodeIndex = nodeIndexOf(node["interfaceString"])
#  snrDict[nodeIndex] = merOf(node["merString"])


#for node in snrDict:
#  print("{}: {}".format(node, snrDict[node]))
