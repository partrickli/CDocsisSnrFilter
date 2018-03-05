#!/usr/bin/env python


import os
import os.path as path

sites = ["gd, js"]


def logFilePaths():
  currentWorkingDirectory = os.getcwd()
  logRootPath = path.join(currentWorkingDirectory, "log")
  logNames = os.listdir(logRootPath)
  logFileNames = os.listdir(logRootPath)
  logFilePaths = [path.join(logRootPath, name) for name in logFileNames]
  return logFilePaths




# serial number collect
def serialNumberOf(line):
  words = line.split()
  nodeIndex = int(words[2].strip())
  serialNumber = words[-1].strip()
  return (nodeIndex, serialNumber)



def serialNumbersOf(logFilePath):
  lines = [l for l in open("./serialNumber") if "frame add" in l]
  serialDict = {}
  for l in lines:
    nodeIndex, serialNumber = serialNumberOf(l)
    serialDict[nodeIndex] = serialNumber
  return serailDict



# snr collect
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


def snrOf(site):

  lines = [l for l in open("./signal")]
  lineCount = len(lines)
  
  filtered = [l.strip() for l in lines if snrRelated(l)]
  
  nodeStrings = []
  for i in range(len(filtered)/2):
    node = {}
    node["interfaceString"] = filtered[i * 2]
    node["merString"] = filtered[i * 2 + 1]
    nodeStrings.append(node)
  
  
def snrOfLog(logFilePath):
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

def logAll():
  threshold = 50
  for node in snrDict:
    if snrDict[node] < threshold:
      print("{}: {}".format(serialDict[node], snrDict[node]))


def main():
  paths = logFilePaths()
  for p in paths:
    print(p)

if __name__ == "__main__":
    main()
