import service_predict_via_heuristics

def predict_type_from_name(property_name, is_fuzzy):
    predicted = service_predict_via_heuristics.predict_type_from_name(property_name, is_fuzzy)

    if (predicted is not None):
        return predicted

    # TODO add more predicters...

    return None
