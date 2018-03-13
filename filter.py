#!/usr/bin/env python


import os
import os.path as path


def logFilePaths():
  currentWorkingDirectory = os.getcwd()
  logRootPath = path.join(currentWorkingDirectory, "log")
  logNames = os.listdir(logRootPath)
  logFileNames = os.listdir(logRootPath)
  logFilePaths = [path.join(logRootPath, name) for name in logFileNames]
  return logFilePaths


# serial number collect
def serialNumberOf(line):
  words = line.strip().split()
  nodeIndex = int(words[2].strip())
  serialNumber = words[-1].strip()
  return (nodeIndex, serialNumber)


def serialNumbersOf(logFilePath):
  lines = [l for l in open(logFilePath) if "frame add" in l]
  serialDict = {}
  for l in lines:
    nodeIndex, serialNumber = serialNumberOf(l)
    serialDict[nodeIndex] = serialNumber
  return serialDict



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


  
  
def snrOfLog(logFilePath, threshold):

  lines = [l for l in open(logFilePath)]
  
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

  snrLowDict = {}
  for node in snrDict:
    if snrDict[node] < threshold:
      snrLowDict[node] = snrDict[node]
  return snrLowDict
  


def printDictionary(dict):
  for key in dict:
    print("{}: {}".format(key, dict[key])) 

def snrLowerThan(threshold, logFilePath):
  serialNumberDict = serialNumbersOf(logFilePath)
  snrLowDict = snrOfLog(logFilePath, 30)
  serialSnrDict = {}
  for node in snrLowDict:
    serialNumer = serialNumberDict[node]
    serialSnrDict[serialNumer] = snrLowDict[node]
  return serialSnrDict
  

def snrThresholdBy(threshold):
  paths = logFilePaths()
  for filePath in paths:
    siteName = filePath.split("/")[-1]
    print("")
    print("------------------{}------------------".format(siteName))
    print(filePath)
    d = snrLowerThan(30, filePath)
    printDictionary(d)

if __name__ == "__main__":
  snrThresholdBy(30)
