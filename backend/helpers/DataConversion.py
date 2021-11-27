import csv
import json


# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath):
    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            # Assuming a column named 'No' to
            # be the primary key
            key = rows['No']
            data[key] = rows
        return json.dumps(data, indent=4)

# write the given json data into the csv file located at csv_path
def write_json_in_csv(csv_path,json):
    data_file = open(csv_path, 'w', newline='')
    csv_writer = csv.writer(data_file)
    count = 0
    for data in json:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(data.values())
    data_file.close()
