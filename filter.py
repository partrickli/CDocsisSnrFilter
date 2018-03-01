#!/usr/bin/env python

def snrRelated(l):
  if "I/F" in l or "MER(dB)" in l:
    return True


snr = {}

lines = [l for l in open("./signal")]
lineCount = len(lines)

filtered = [l.strip() for l in lines if snrRelated(l)]
nodeStrings = [(filtered[i], filtered[i+1]) for i in range(len(filtered)/2)]
for s in nodeStrings:
  print("node")
  print(s)



