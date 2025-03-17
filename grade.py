def calculate(number_grade):
    # Handle invalid inputs
    if number_grade < 0 or number_grade > 100:
        return "N/A"
    
    # Convert to letter grade based on ranges
    if number_grade >= 90:
        return "A"
    elif number_grade >= 80:
        return "B"
    elif number_grade >= 70:
        return "C"
    elif number_grade >= 60:
        return "D"
    else:
        return "F"