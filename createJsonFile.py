import csv
import json
import ast


def read_csv(file):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        data_size = 0
        for row in reader:
            latitude_longitude = []
            crime_event = []
            crime_date = row[title[1]]
            if "2019" in crime_date:
                data_size=data_size+1
                location = ast.literal_eval(row[title[16]])
                event = row[title[13]]
                #event="abcd"
                latitude_longitude.append(float(location.get('longitude')))
                latitude_longitude.append(float(location.get('latitude')))
                print(latitude_longitude)
                csv_rows.extend([{"location":latitude_longitude, "crimeEvent":event}])  
        print("data size:", data_size)
        return csv_rows

# json
def write_json(data, json_file):
    with open(json_file, "w") as f:
            f.write(json.dumps(data))

write_json(read_csv('../data/arrest-data-from-2010-to-present.csv'), '../data/crime_coordinates.js')
