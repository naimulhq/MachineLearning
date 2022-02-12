import csv

CSV_TRAIN_FILE_LOCATION = r"titanic.csv"

def read_csv_data(csv_file):
    titanic_data = []
    with open(csv_file, newline='') as titanic_csv:
        csv_file_reader = csv.reader(titanic_csv)
        for row in csv_file_reader:
            titanic_data.append(row)



if __name__ == '__main__':
    train_data = read_csv_data(CSV_TRAIN_FILE_LOCATION)
    