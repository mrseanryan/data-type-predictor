"""
evaluate.py <JSON file path OR glob> [--help --fuzzy]
"""
# Evaluate accuracy against a data set
import glob
from optparse import OptionParser

import service_predict_type_from_name
import util_file

#usage() - prints out the usage text, from the top of this file :-)
def print_usage():
    print(__doc__)

parser = OptionParser(usage=__doc__)
parser.add_option("-f", "--fuzzy", dest="is_fuzzy",
    action='store_const',
    const=True, default=False,
    help="Apply fuzzy matching")

(options, args) = parser.parse_args()

if len(args) != 1:
    print_usage()
    exit(1)

INPUT_GLOB = args[0]

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
        predicted_type = service_predict_type_from_name.predict_type_from_name(property_name, options.is_fuzzy)
        if (predicted_type == expected_property_type):
            hits = hits + 1
        else:
            if predicted_type is None:
                not_predicted = not_predicted + 1
            else:
                misses = misses + 1
        total_names = total_names + 1

def calculate_accuracy(tp, fp):
    return calculate_percent(tp, tp + fp)

options_summary = ""
if options.is_fuzzy:
    options_summary = "(fuzzy matching is enabled)"

print(f"# Evaluation: {options_summary}")
print()
print(f"Accuracy = TP/(TP+FP) = {calculate_accuracy(hits, misses)}%")
print()
print(f"{calculate_percent(hits, total_names)}% correctly predicted")
print(f"{calculate_percent(misses, total_names)}% incorrectly predicted")
print(f"{calculate_percent(not_predicted, total_names)}% not predicted")
print(f"Data set size: {total_names} words")
