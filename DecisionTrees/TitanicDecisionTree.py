import csv
import math

CSV_TRAIN_FILE_LOCATION = r"titanic.csv"
IGNORE_ATTRIBUTE = ["Name"]
CONTINUOUS_ATTRIBUTES = ["Fare", "Age"]
CATEGORICAL_ATTRIBUTES = ["Survived", "Sex", "Pclass", "Siblings/Spouses Aboard", "Parents/Children Aboard"]

class TitanicDecisionTree:

    def __init__(self):
        pass

    # This is for categorical attribute. Function will differ for continous attributes
    def calculate_categorical_entropy(self, data, result = None):
        # Entropy = summation (p_i)log_2(pi_i)

        temporary_map = {}
        total = len(data)
        entropy = 0


        # Collect all data
        for index,value in enumerate(data):
            if value not in temporary_map.keys():
                temporary_map[value] = [0,0,0]
                temporary_map[value][2] += 1
                if int(result[index]) == 1:
                    temporary_map[value][0] += 1
                else:
                    temporary_map[value][1] += 1
            else:
                temporary_map[value][2] += 1
                if int(result[index]) == 1:
                    temporary_map[value][0] += 1
                else:
                    temporary_map[value][1] += 1

        for key in temporary_map.keys():
            analysis = temporary_map[key]
            survive_probability_for_attribute = analysis[0]/analysis[2]
            death_probability_for_attribute = analysis[1]/analysis[2]
            entropy_for_attribute = survive_probability_for_attribute * math.log(survive_probability_for_attribute,2) + death_probability_for_attribute * math.log(death_probability_for_attribute,2)
            entropy_for_attribute = -1 * entropy_for_attribute
            entropy += entropy_for_attribute * ((analysis[2]) / total)

        del temporary_map

        return entropy

    def calculate_continous_entropy(self, data, result, threshold):
        greater_than_equal_total = 0
        greater_than_equal_dead = 0
        greater_than_equal_survive = 0
        less_than_total = 0
        less_than_survive = 0
        less_than_dead = 0
        for index,value in enumerate(data):
            if float(value) >= float(threshold):
                greater_than_equal_total += 1
                if int(result[index]) == 1:
                    greater_than_equal_survive += 1
                else:
                    greater_than_equal_dead += 1
            else:
                less_than_total += 1
                if int(result[index]) == 1:
                    less_than_survive += 1
                else:
                    less_than_dead += 1
        print(greater_than_equal_total,greater_than_equal_survive,greater_than_equal_dead,less_than_total,less_than_dead,less_than_survive)
        probability_greater_than_equal_survive = greater_than_equal_survive / greater_than_equal_total
        probability_greater_than_equal_dead = 1 - probability_greater_than_equal_survive
        probability_less_than_survive = less_than_survive / less_than_total
        probability_less_than_dead = 1 - probability_less_than_survive

        entropy_greater_than_equal = probability_greater_than_equal_survive * math.log(probability_greater_than_equal_survive,2) + probability_greater_than_equal_dead * math.log(probability_greater_than_equal_dead,2)
        entropy_greater_than_equal = -1 * entropy_greater_than_equal
        entropy_less_than = probability_less_than_survive * math.log(probability_less_than_survive,2) + probability_less_than_dead * math.log(probability_less_than_dead,2)
        entropy_less_than = -1 * entropy_less_than

        entropy = ((greater_than_equal_total / (greater_than_equal_total + less_than_total)) * entropy_greater_than_equal) + ((less_than_total/(greater_than_equal_total + less_than_total)) * entropy_less_than)
        return entropy

    def calculate_information_gain(self):

        pass

    def calculate_parent_entropy(self, data):
        entropy = 0
        total_survived = 0
        total_dead = 0
        for value in data:
            if int(value) == 1:
                total_survived += 1
            else:
                total_dead += 1
        probability_dead = total_dead / (total_survived + total_dead)
        probability_survived = total_survived / (total_survived + total_dead)
        entropy_dead = probability_dead * math.log(probability_dead,2)
        entropy_alive = probability_survived * math.log(probability_survived,2)
        entropy = entropy_dead + entropy_alive
        print("Parent Entropy: ", entropy * -1)
        return -1 * entropy

    def train(self, train_data):
        parent_entropy = self.calculate_parent_entropy(train_data[0][1:])
        while parent_entropy != 0:
            information_gain = []
            column_index_start = 1
            for column in range(column_index_start,len(train_data)):
                if train_data[column][0] in CATEGORICAL_ATTRIBUTES:
                    data = train_data[column][1:]
                    entropy = self.calculate_categorical_entropy(data, train_data[0][1:])
                    print(f"Value {train_data[column][0]} IG {parent_entropy - entropy}")
                    information_gain.append(parent_entropy - entropy)
                elif train_data[column][0] in IGNORE_ATTRIBUTE:
                    continue
                else:
                    data = train_data[column][1:]
                    data_visited = []
                    thresholds = []
                    data_sorted = sorted(data)
                    max_information_gain = 0
                    max_threshold = None

                    for index in range(len(data_sorted)-1):
                        if float(data_sorted[index]) != float(data_sorted[index+1]):
                            avg = (float(data_sorted[index]) + float(data_sorted[index+1]))/2
                            thresholds.append(avg)                      
                    for value in thresholds:
                        if value in data_visited:
                            continue
                        else:
                            entropy = self.calculate_continous_entropy(train_data[column][1:], train_data[0][1:], value)
                            if (parent_entropy - entropy) > max_information_gain:
                                max_information_gain = (parent_entropy - entropy)
                                max_threshold = value
                            data_visited.append(value)
                    print(max_information_gain,max_threshold)
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