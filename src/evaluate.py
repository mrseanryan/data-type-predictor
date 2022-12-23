# Evaluate accuracy against a data set
import glob
import sys

import service_predict_type_from_name
import util_file

if len(sys.argv) < 2:
    print(f"USAGE: {sys.argv[0]} <JSON file path OR glob>")
    exit(1)

INPUT_GLOB = sys.argv[1]

def calculate_percent(numerator, denominator):
    return round((numerator * 100) / denominator)

total_names = 0
hits = 0
misses = 0
not_predicted = 0

for json_file_path in glob.glob(INPUT_GLOB):
    entries = util_file.read_json_file(json_file_path)["data"]
    for entry in entries:
        property_name = entry["name"]
        expected_property_type = entry["data_type"]
        predicted_type = service_predict_type_from_name.predict_type_from_name(property_name)
        if (predicted_type == expected_property_type):
            hits = hits + 1
        else:
            if predicted_type is None:
                not_predicted = not_predicted + 1
            else:
                misses = misses + 1
        total_names = total_names + 1

print("# Accuracy:")
print()
print(f"{calculate_percent(hits, total_names)}% correctly predicted")
print(f"{calculate_percent(misses, total_names)}% incorrectly predicted")
print(f"{calculate_percent(not_predicted, total_names)}% not predicted")
print(f"Data set size: {total_names} words")
