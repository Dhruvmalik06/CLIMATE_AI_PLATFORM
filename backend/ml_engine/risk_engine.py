def risk_reasoning(pred, climate_context):

    if pred == 2:
        return {
            "level":"Severe",
            "action":"Emergency alert + disaster preparation",
            "impact":"Floods, crop damage, infrastructure risk"
        }

    if pred == 1:
        return {
            "level":"Moderate",
            "action":"Advisory + resource planning",
            "impact":"Heat stress, water shortages"
        }

    return {
        "level":"Normal",
        "action":"Monitoring only",
        "impact":"Stable climate"
    }
