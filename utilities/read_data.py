import csv


def getCSVData(fileName):
    # Create an empty list to store rows
    rows = []
    # Open the csv file
    dataFile = open(fileName, "r")
    # Create a csv reader from CSV file
    reader = csv.reader(dataFile)
    # Skip the headers
    next(reader)
    # Add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows
