def generate_recommendation(
    predicted_consumption,
    efficiency_score,
    reactive_ratio,
    hour,
    sub_metering_2,
    sub_metering_3
):
    """
    Generate optimization recommendations based on energy patterns.
    """

    recommendations = []
    estimated_savings = 0

    # Peak hour load shifting
    if hour in range(18, 23) and predicted_consumption > 4.5:
        recommendations.append(
            "High energy usage during peak hours. Consider shifting heavy appliances to off-peak hours."
        )
        estimated_savings += 10

    # Reactive power inefficiency
    if reactive_ratio > 0.35:
        recommendations.append(
            "High reactive power detected. Check for inefficient appliances or power factor correction."
        )
        estimated_savings += 8

    # Laundry optimization
    if sub_metering_2 > 1.5:
        recommendations.append(
            "Laundry appliances consuming high energy. Run washing machines during off-peak hours."
        )
        estimated_savings += 6

    # HVAC / Heater optimization
    if sub_metering_3 > 2.0:
        recommendations.append(
            "HVAC or water heating load is high. Optimize thermostat settings or usage duration."
        )
        estimated_savings += 12

    # Overall efficiency assessment
    if efficiency_score < 60:
        recommendations.append(
            "Overall efficiency is low. Consider an energy audit for the household."
        )
        estimated_savings += 5

    if not recommendations:
        recommendations.append(
            "Energy usage is within optimal range. No immediate action required."
        )

    return {
        "recommendations": recommendations,
        "estimated_savings_percent": min(estimated_savings, 30)
    }
