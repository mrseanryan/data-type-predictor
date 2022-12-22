import re

import util_list

def camel_case_split(str):
    return re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)

def camel_case_split_starts_lower(str):
    str_starts_upper = str[0].upper() + str[1:]
    return camel_case_split(str_starts_upper)

def to_lower_list(items):
    lower_items = []
    for item in items:
        lower_items.append(item.lower())
    return lower_items

def camel_case_split_lower(str):
    tokens = to_lower_list(camel_case_split(str))
    tokens_starts_lower = to_lower_list(camel_case_split_starts_lower(str))
    return util_list.add_lists_no_duplicates(tokens_starts_lower, tokens)
