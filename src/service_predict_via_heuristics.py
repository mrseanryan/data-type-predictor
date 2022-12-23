import data_types
import service_stemmer
import service_fuzzy_match

def is_matching(word, other_words, is_fuzzy):
    if is_fuzzy:
        return service_fuzzy_match.is_fuzzy_match_list(word, other_words)
    return word in other_words

def _predict_type_from_name_can_be_fuzzy(property_name, is_fuzzy, first_token, last_token):

    booleanTokens = ["is", "can", "should", "did", "was", "active", "ignore"]
    if is_matching(first_token, booleanTokens, is_fuzzy):
        return data_types.Boolean()

    integerSuffixTokens = ["number", "nr", "height", "width", "length", "depth", "speed", "velocity", "priority", "count"]
    if is_matching(last_token, integerSuffixTokens, is_fuzzy):
        return data_types.Integer()
    
    integerPrefixTokens = ["nr"]
    if is_matching(first_token, integerPrefixTokens, is_fuzzy):
        return data_types.Integer()
    
    decimalTokens = ["balance", "amount"]
    if is_matching(first_token, decimalTokens, is_fuzzy) or is_matching(last_token, decimalTokens, is_fuzzy):
        return data_types.Decimal()

    dateSuffixTokens = ["date", "at", "on"]
    if is_matching(last_token, dateSuffixTokens, is_fuzzy):
        return data_types.Date()

    datePrefixTokens = ["date"]
    if is_matching(first_token, datePrefixTokens, is_fuzzy):
        return data_types.Date()

    if property_name.endswith('en') or property_name.endswith('ed'):
        return data_types.Boolean()

    language_codes = ["EN", "NL"]
    for language_code in language_codes:
        if property_name.endswith(language_code):
            return data_types.String()

    string_suffixes = ["name", "password", "code", "by", "email", "address"]
    if is_matching(last_token, string_suffixes, is_fuzzy):
        return data_types.String()

    enumeration_tokens = ["color", "status", "type", "category"]
    if is_matching(first_token, enumeration_tokens, is_fuzzy) or is_matching(last_token, enumeration_tokens, is_fuzzy):
        return data_types.Enumeration()

    return None

def predict_type_from_name(property_name):
    tokens = service_stemmer.camel_case_split_lower(property_name)
    if len(tokens) == 0:
        return None

    first_token = tokens[0]
    last_token = tokens[-1]

    # Run exact match first, then try fuzzy
    prediction = _predict_type_from_name_can_be_fuzzy(property_name, False, first_token, last_token)
    if prediction is None:
        prediction = _predict_type_from_name_can_be_fuzzy(property_name, True, first_token, last_token)

    return prediction
