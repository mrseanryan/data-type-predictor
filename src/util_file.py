import json

def read_json_file(json_file_path):
    with open(json_file_path, encoding='utf8') as file:
        # returns JSON object as a dictionary
        data = None
        try:
            data = json.load(file)
        except:
            print(f"[error] could not load json from {file}")
        return data

def write_json_file(json_file_path, json_data):
    json_object = json.dumps(json_data, indent=2)
    with open(json_file_path, 'w', encoding='utf8') as json_file:
        return json_file.write(json_object)
