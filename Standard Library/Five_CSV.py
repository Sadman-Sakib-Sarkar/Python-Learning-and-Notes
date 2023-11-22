#CSV: Common Separated Value

import csv

## We will avoid this file open approach:

# file = open("Standard Library/subfolder5/data.csv", "w")
# file.close() #after done need to close.

## We will use the following approach for opening a file:
## Creating the csv file:

# with open("Standard Library/subfolder5/data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1001, 2, 15])

## Reading from the csv file:

with open("Standard Library/subfolder5/data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader)) #This method takes the cursor to the end
    for row in reader:
        print(row) #for printing the rows we need to comment out 'print(list(reader))'

