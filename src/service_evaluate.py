import glob

import service_predict_type_from_name
import util_file
import util_number

def calculate_accuracy(tp, fp):
    return util_number.calculate_percent(tp, tp + fp)

class EvaluationResult:
    def __init__(self, accuracy, total_names, hits, misses, not_predicted) -> None:
        self.accuracy = accuracy
        self.total_names = total_names
        self.hits = hits
        self.misses = misses
        self.not_predicted = not_predicted

def evaluate_accuracy(input_glob, is_fuzzy):
    total_names = 0
    hits = 0
    misses = 0
    not_predicted = 0

    for json_file_path in glob.glob(input_glob):
        entries = util_file.read_json_file(json_file_path)["data"]
        for entry in entries:
            property_name = entry["name"]
            expected_property_type = entry["data_type"]
            predicted_type = service_predict_type_from_name.predict_type_from_name(property_name, is_fuzzy)
            if (predicted_type == expected_property_type):
                hits = hits + 1
            else:
                if predicted_type is None:
                    not_predicted = not_predicted + 1
                else:
                    misses = misses + 1
            total_names = total_names + 1
    accuracy = calculate_accuracy(hits, misses)
    return EvaluationResult(accuracy, total_names, hits, misses, not_predicted)
