import data_types
import service_stemmer

def predict_type_from_name(property_name):
    tokens = service_stemmer.camel_case_split_lower(property_name)
    if len(tokens) == 0:
        return None

    first_token = tokens[0]
    last_token = tokens[-1]

    booleanTokens = ["is", "can", "should", "did", "was", "active", "ignore"]

    if first_token in booleanTokens:
        return data_types.Boolean()

    integerSuffixTokens = ["number", "nr", "height", "width", "length", "depth", "speed", "velocity", "priority"]
    if last_token in integerSuffixTokens:
        return data_types.Integer()
    
    integerPrefixTokens = ["nr"]
    if first_token in integerPrefixTokens:
        return data_types.Integer()
    
    decimalTokens = ["balance", "amount"]
    if first_token in decimalTokens or last_token in decimalTokens:
        return data_types.Decimal()
    return None