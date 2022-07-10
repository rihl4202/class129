import csv

data = []
with open("archive_dataset.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)

headers = data[0]
planetdata = data[1:]

for datapoint in planetdata:
    datapoint[2] = datapoint[2].lower()
planetdata.sort(key = lambda planetdata:planetdata[2])

with open("archive_dataset_sorted.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)

with open ("archive_dataset_sorted.csv") as input,open("archive_dataset_sorted_1.csv","w") as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)