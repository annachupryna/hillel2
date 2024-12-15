# Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
# Результат запишіть у файл result_<your_second_name>.csv


def remove_duplicates_in_csv(file1, file2, output_file):
    def read_csv(file_path):
        with open(file_path, 'r') as f:
            return [line.strip() for line in f.readlines()]

    def write_csv(file_path, data):
        with open(file_path, 'w') as f:
            f.writelines(line + '\n' for line in data)

    data1 = read_csv(file1)
    data2 = read_csv(file2)

    unique_data = list(set(data1 + data2))

    write_csv(output_file, unique_data)


file1_path = 'r-m-c.csv'
file2_path = 'rmc.csv'
output_file_path = 'result.csv'

remove_duplicates_in_csv(file1_path, file2_path, output_file_path)
