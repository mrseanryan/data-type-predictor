import service_predict_via_heuristics

def predict_type_from_name(property_name):
    predicted = service_predict_via_heuristics.predict_type_from_name(property_name)

    if (predicted is not None):
        return predicted

    # TODO add more predicters...

    return None
