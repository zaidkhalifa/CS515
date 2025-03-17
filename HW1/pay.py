# Round down hours to nearest whole number using int() and calculate the pay at $15 per hour
def unfair_weekly_paycheck_amount(hours):
    # Return a 0 for negative inputs, since you can't work negative hours.
    if hours < 0:
        return 0
    return int(hours) * 15

# Calculate the pay directly with a float value at $15.0 per hour
def fair_weekly_paycheck_amount(hours):
    if hours < 0:
        return 0.0
    return hours * 15.0