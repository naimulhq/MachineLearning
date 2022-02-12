import csv

CSV_TRAIN_FILE_LOCATION = r"titanic.csv"

class TitanicDecisionTree:

    def __init__(self):
        pass

    def train(self, train_data):
        pass

    def test(self, test_data):
        pass

def read_csv_data(csv_file):
    titanic_data = []
    with open(csv_file, newline='') as titanic_csv:
        csv_file_reader = csv.reader(titanic_csv)
        for row in csv_file_reader:
            titanic_data.append(row)
    return titanic_data

def parse_csv_data(data):
    parsed_data = []
    total_columns = len(data[0])

    for column in range(total_columns):
        parsed_data.append([])
    
    for row in data:
        for column in range(len(row)):
            parsed_data[column].append(row[column])
    
    return parsed_data


if __name__ == '__main__':
    train_data = read_csv_data(CSV_TRAIN_FILE_LOCATION)
    parsed_train_data = parse_csv_data(train_data)
    del train_data
    titanic_decision_tree = TitanicDecisionTree()
    titanic_decision_tree.train(parsed_train_data)
    titanic_decision_tree.test()