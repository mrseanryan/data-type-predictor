import sys

import service_predict_type_from_name

if len(sys.argv) < 2:
    print(f"USAGE: {sys.argv[0]} <property name>")
    exit(1)

PROPERTY_NAME = sys.argv[1]

predicted_type = service_predict_type_from_name.predict_type_from_name(PROPERTY_NAME)

print(f"{PROPERTY_NAME}={predicted_type}")
