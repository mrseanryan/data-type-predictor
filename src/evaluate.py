"""
evaluate.py <JSON file path OR glob> [--help --fuzzy]
"""
# Evaluate accuracy against a data set
from optparse import OptionParser

import service_evaluate
import util_number

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

options_summary = ""
if options.is_fuzzy:
    options_summary = "(fuzzy matching is enabled)"

result = service_evaluate.evaluate_accuracy(INPUT_GLOB, options.is_fuzzy)

print(f"# Evaluation: {options_summary}")
print()
print(f"Accuracy = TP/(TP+FP) = {result.accuracy}%")
print()
print(f"{util_number.calculate_percent(result.hits, result.total_names)}% correctly predicted")
print(f"{util_number.calculate_percent(result.misses, result.total_names)}% incorrectly predicted")
print(f"{util_number.calculate_percent(result.not_predicted, result.total_names)}% not predicted")
print(f"Data set size: {result.total_names} words")
