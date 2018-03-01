#!/usr/bin/env python

def snrRelated(l):
  if "I/F" in l or "MER(dB)" in l:
    return True

def merOf(line):
  merString = line.split(":")[1]
  mer = float(merString.strip())
  return mer
  

def nodeIndexOf(line):
  interfaceString = line.split(":")[1].strip()
  nodeIndex = int(interfaceString.split("/")[0])
  return nodeIndex


# main

# snr collect
lines = [l for l in open("./signal")]
lineCount = len(lines)

filtered = [l.strip() for l in lines if snrRelated(l)]

nodeStrings = []
for i in range(len(filtered)/2):
  node = {}
  node["interfaceString"] = filtered[i * 2]
  node["merString"] = filtered[i * 2 + 1]
  nodeStrings.append(node)



snrDict = {}

for node in nodeStrings:
  nodeIndex = nodeIndexOf(node["interfaceString"])
  currentMer = merOf(node["merString"])
  # just keep record the minimum snr
  if nodeIndex not in snrDict:
    snrDict[nodeIndex] = currentMer
  else:
    if currentMer < snrDict[nodeIndex]:
      snrDict[nodeIndex] = currentMer


# SNR Threshold
threshold = 35
for node in snrDict:
  if snrDict[node] < threshold:
    print("{}: {}".format(node, snrDict[node]))

