import os, glob, hashlib
import json

targetDir = './data'
fileDict = {}

# ファイルの一覧
files = glob.glob(targetDir + "/*")
for f in files:
    print(f)
    fileDict[f] = glob.glob(f + "/*.txt")

print(fileDict)
print(json.dumps(fileDict))

result = [[f'{num1 * num2:2}' for num2 in range(1, 10)] for num1 in range(1, 10)]

for count, row in zip(range(1, 10), result):
    print(', '.join(row))