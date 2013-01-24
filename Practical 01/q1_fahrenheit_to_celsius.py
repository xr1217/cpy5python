# Filename: q1_fahrenheit_to_celsius.py
# Author: Chia Xiang Rong
# Date created: 22/1/2013
# Date modified: 22/1/2013
# Description: Convert Fahrenheit degree in double to Celsius

# Prompt input of Fahrenheit degree in double
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert to Celsius
celsius = (5/9) * (fahrenheit - 32)

# Display Celsius degeee
print ("Temperature in Celsius (to nearest degree): {0:.0f}".format(celsius))
