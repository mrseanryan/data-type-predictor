"""
REPL - Given the name of a property or attribute like 'BrandName' or 'AmountReceived', try to predict a data type like String, Boolean, Integer...

predict-type-from-name-repl.py [--help --fuzzy]
"""
from optparse import OptionParser

import service_predict_type_from_name

#usage() - prints out the usage text, from the top of this file :-)
def print_usage():
    print(__doc__)

parser = OptionParser(usage=__doc__)
parser.add_option("-f", "--fuzzy", dest="is_fuzzy",
    action='store_const',
    const=True, default=False,
    help="Apply fuzzy matching")

(options, args) = parser.parse_args()

if len(args) != 0:
    print_usage()
    exit(1)

options_summary = ""
if options.is_fuzzy:
    options_summary = "(fuzzy matching is enabled)"

print("Enter a property name like 'Color' or 'BrandName' or 'CreatedOn'")
print(options_summary)

def input_next_property_name():
    return input("(just press ENTER to exit) ->")

PROPERTY_NAME = input_next_property_name()
while(len(PROPERTY_NAME) > 0):
    predicted_type = service_predict_type_from_name.predict_type_from_name(PROPERTY_NAME, options.is_fuzzy)
    print(f"{PROPERTY_NAME}={predicted_type}")
    PROPERTY_NAME = input_next_property_name()
