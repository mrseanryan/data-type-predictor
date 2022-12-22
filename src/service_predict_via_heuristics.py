import data_types
import service_stemmer

def predict_type_from_name(property_name):
    tokens = service_stemmer.camel_case_split_lower(property_name)
    if len(tokens) == 0:
        return None

    first_token = tokens[0]

    booleanTokens = ["is", "can", "should", "did"]

    if first_token in booleanTokens:
        return data_types.boolean()
