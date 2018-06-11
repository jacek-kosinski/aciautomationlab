import csv

with open('app-configs.csv') as csvFile:
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        print "AppProfile:", row[0]
        print "VRF:", row[1]
        print "BD:", row[2]
        print "Subnet:", row[3]
        print
