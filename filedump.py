import os
import csv

csv_file_path = "file.csv"

folder_path = "/Users/user/desktop/company"

with open(csv_file_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    file_names = [row[0] for row in csv_reader]

folder_file_names = os.listdir(folder_path)

for file_name in folder_file_names:
    if file_name in file_names:
        print(f"{file_name} matched, will be preserved.")
    else:
        file_path = os.path.join(folder_path, file_name)
        os.remove(file_path)
        print(f"{file_name} deleted.")
