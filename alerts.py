def assess_risk(people, pets, radar_present, vehicle_parked,
                parked_minutes, cabin_temp):
    """
    Simple explainable prototype risk score.
    This is a demonstration rule-set, not a validated safety model.
    """
    score = 0
    reasons = []

    if people > 0:
        score += 35
        reasons.append("Person detected in cabin")
    if pets > 0:
        score += 35
        reasons.append("Pet detected in cabin")
    if radar_present:
        score += 15
        reasons.append("Radar occupancy confirmation enabled")
    if vehicle_parked and parked_minutes >= 5 and (people > 0 or pets > 0):
        score += 10
        reasons.append("Vehicle parked for at least 5 minutes with detected occupant")
    if cabin_temp >= 35:
        score += 25
        reasons.append("High cabin temperature")
    elif cabin_temp >= 30:
        score += 10
        reasons.append("Elevated cabin temperature")

    score = min(score, 100)
    if score >= 60:
        level = "HIGH"
    elif score >= 30:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {"score": score, "level": level, "reasons": reasons}


def build_alert(risk):
    if risk["level"] == "HIGH":
        message = "HIGH RISK: Check the cabin immediately."
    elif risk["level"] == "MEDIUM":
        message = "CAUTION: Occupancy or cabin conditions need attention."
    else:
        message = "LOW RISK: No high-risk condition identified by this prototype."

    if risk["reasons"]:
        message += " Reasons: " + "; ".join(risk["reasons"]) + "."
    return {"level": risk["level"], "message": message}
