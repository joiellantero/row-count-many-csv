import os
import csv
import argparse

parser = argparse.ArgumentParser(description='Quickly count number of entries (rows excluding header) in multiple .csv files')

parser.add_argument(
    'filepath',
    metavar='filepath',
    type=str,
    help='The folder where all the csv files are located. Enclose the filepath with quotation marks if there are spaces.'
)

args = parser.parse_args()

path = args.filepath
files = [file for file in os.listdir(path) if file.endswith(".csv")]

output = dict()
for file in files:
    with open(os.path.join(path, file)) as f:
        reader = csv.reader(f)
        output[file.replace(".csv", "")] = sum(1 for row in reader)-1
output["Total"] = sum(output.values())

print(output)
