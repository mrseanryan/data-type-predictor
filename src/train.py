"""
Train against a data set, by evaluating Accuracy across the combination of parameters.

train.py <JSON file path OR glob> [--help --fuzzy]
"""
from optparse import OptionParser

from config_fuzzy_match import FuzzyMatchConfig

import service_evaluate

#usage() - prints out the usage text, from the top of this file :-)
def print_usage():
    print(__doc__)

parser = OptionParser(usage=__doc__)
parser.add_option("-f", "--force_fuzzy", dest="force_fuzzy",
    action='store_const',
    const=True, default=False,
    help="Force fuzzy matching")

(options, args) = parser.parse_args()

if len(args) != 1:
    print_usage()
    exit(1)

INPUT_GLOB = args[0]

# The Cost function used to optimize
def cost_function(result):
    return 100 - result.accuracy

# Define the search space that we need to optimize
#
# FuzzyMatchConfig.MAX_DISTANCE
MAX_DISTANCES = range(0, 10)
#
# FuzzyMatchConfig.MIN_LENGTH
MIN_LENGTHS = range(2, 10)

fuzzy_values = [False, True]
if options.force_fuzzy:
    fuzzy_values = [True]
    MAX_DISTANCES = range(1, 10)

class TrainingConfig:
    def __init__(self, is_fuzzy, max_distance, min_length, cost, accuracy) -> None:
        self.is_fuzzy = is_fuzzy
        self.max_distance = max_distance
        self.min_length = min_length
        self.cost = cost
        self.accuracy = accuracy
    
    def is_cheaper_than(self, other):
        return self.cost < other.cost
    
    def __str__(self) -> str:
        return f"is_fuzzy={self.is_fuzzy}, max_distance={self.max_distance}, min_length={self.min_length}, cost={self.cost}, accuracy={self.accuracy}"

optimal_config = None

print("Training...")

for is_fuzzy in fuzzy_values:
    for max_distance in MAX_DISTANCES:
        for min_length in MIN_LENGTHS:
            FuzzyMatchConfig.MAX_DISTANCE = max_distance
            FuzzyMatchConfig.MIN_LENGTH = min_length
            result = service_evaluate.evaluate_accuracy(INPUT_GLOB, is_fuzzy)
            cost = cost_function(result)
            this_config = TrainingConfig(is_fuzzy, max_distance, min_length, cost, result.accuracy)
            if (optimal_config is None):
                optimal_config = this_config
            else:
                if (this_config.is_cheaper_than(optimal_config)):
                    optimal_config = this_config

print("[done]")

print(f"Optimal config:")
print(optimal_config)
