import csv

with open('qset1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',') 
    print(readCSV)

    for row in read:
        print(row['Questions'], row['Answers'], row['Categories'], row['Score'])