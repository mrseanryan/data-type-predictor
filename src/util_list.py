def add_no_duplicates(list1, item):
    if not item in list1:
        return list1 + [item]
    return list1

def add_lists_no_duplicates(list1, list2):
    new_list = []
    for item in list1:
        new_list = add_no_duplicates(new_list, item)
    for item in list2:
        new_list = add_no_duplicates(new_list, item)
    return new_list
