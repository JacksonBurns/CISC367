import csv

with open('data/KaggleData.csv','r',errors='ignore') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)