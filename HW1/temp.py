#function to convert
def fahrenheit_to_celsius(temp_f):
    return (temp_f - 32) * 5/9

# Get input
fahrenheit_str = input("Enter temperature in Fahrenheit: ")

# Convert input to float
temp_fahrenheit = float(fahrenheit_str)

# Convert to Celsius
temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)

# Print result
print(f"Temperature in Celsius: {temp_celsius:.1f}")