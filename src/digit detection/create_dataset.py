import glob
import csv
import os

row = [
    ['Image Path', 'Digit']
  ]

for folder in os.listdir(r"src\digit detection\data"):
  for items in os.listdir(r"src\digit detection\data" + "\\" + str(folder)):
    print(items)
    row.append([r"src\digit detection\data" + "\\" + str(folder) + "\\" + str(items), folder])

file = open(r"src\digit detection\data\dataset.csv", 'w')
writer = csv.writer(file)
writer.writerows(row)
print('File generated successfully...')
