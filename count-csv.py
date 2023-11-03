import os
import csv

path = "./test2"
files = [file for file in os.listdir(path) if file.endswith(".csv")]

output = dict()
for file in files:
    with open(os.path.join(path, file)) as f:
        reader = csv.reader(f)
        output[file.replace(".csv", "")] = sum(1 for row in reader)-1
output["Total"] = sum(output.values())

print(output)