import sys

import service_predict_type_from_name

def input_next_property_name():
    return input("Enter a property name like 'Color' or 'BrandName' or 'CreatedOn' (just press ENTER to exit) ->")

PROPERTY_NAME = input_next_property_name()
while(len(PROPERTY_NAME) > 0):
    predicted_type = service_predict_type_from_name.predict_type_from_name(PROPERTY_NAME)
    print(f"{PROPERTY_NAME}={predicted_type}")
    PROPERTY_NAME = input_next_property_name()
