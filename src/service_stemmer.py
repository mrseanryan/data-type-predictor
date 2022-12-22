import re

def camel_case_split(str):
    return re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)

def camel_case_split_lower(str):
    tokens = camel_case_split(str)
    lower_case_tokens = []
    for token in tokens:
        lower_case_tokens.append(token.lower())
    return lower_case_tokens
