import csv
import math

CSV_TRAIN_FILE_LOCATION = r"titanic.csv"
IGNORE_ATTRIBUTE = ["Name"]
CONTINUOUS_ATTRIBUTES = ["Fare", "Age", "Pclass", "Siblings/Spouses Aboard", "Parents/Children Aboard"]
CATEGORICAL_ATTRIBUTES = ["Survived", "Sex"]

class TitanicDecisionTree:

    def __init__(self):
        pass

    # This is for categorical attribute. Function will differ for continous attributes
    def calculate_categorical_entropy(self,data):
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
            print(probability_of_value_attribute,entropy_of_value_attribute,key)
        print(-1 * entropy)
        del temporary_map
        return -1 * entropy
        
    def calculate_continous_entropy(self, data, threshold):
        pass


    def calculate_information_gain(self):
        pass

    def train(self, train_data):
        parent_entropy = self.calculate_categorical_entropy(train_data[0][1:])
        while parent_entropy != 0:
            information_gain = []
            column_index_start = 1
            for column in range(column_index_start,len(train_data)):
                if train_data[column][0] in CATEGORICAL_ATTRIBUTES:
                    data = train_data[column][1:]
                    entropy = self.calculate_categorical_entropy(data)
                    information_gain.append(parent_entropy - entropy)
                else:
                    data = train_data[column][1:]
                    data_visited = []
                    data_sorted = sorted(data)
                    max_information_gain = 0
                    max_threshold = None
                    for value in data_sorted:
                        if value in data_visited:
                            continue
                        else:
                            entropy = self.calculate_continous_entropy(train_data, value)
                            if (parent_entropy - entropy) > max_information_gain:
                                max_information_gain = (parent_entropy - entropy)
                                max_threshold = value
                            data_visited.append(value)
                    information_gain.append(max_information_gain)
            print(information_gain)
            exit()

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