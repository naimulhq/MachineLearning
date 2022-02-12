import csv
import math

CSV_TRAIN_FILE_LOCATION = r"titanic.csv"

class TitanicDecisionTree:

    def __init__(self):
        pass

    def calculate_entropy(self,data):
        # Entropy = summation (p_i)log_2(pi_i)

        temporary_map = {}
        total = len(data)
        entropy = 0
        for value in data:
            if value not in temporary_map.keys():
                temporary_map[value] = 1
            else:
                temporary_map[value] += 1
        

        for key in temporary_map.keys():
            probability_of_value_attribute = temporary_map[key] / total
            entropy_of_value_attribute =  probability_of_value_attribute * math.log(probability_of_value_attribute,2)
            entropy += entropy_of_value_attribute
        
        return -1 * entropy
        


    def calculate_information_gain(self):
        pass

    def train(self, train_data):
        parent_entropy = self.calculate_entropy(train_data[0][1:])
        print(parent_entropy)
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
    #titanic_decision_tree.test()