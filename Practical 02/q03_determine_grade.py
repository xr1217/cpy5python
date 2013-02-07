# Filename: q03_determine_grade.py
# Author: Chia Xiang Rong
# Date created: 29/1/13
# Date modified: 29/1/13
# Description: Displays grade based on score inputted.

#Input of score
score = float(input("Enter score: "))

#Determine and display grade
if score < 0 or score > 100:
    print("Invalid! Score should be within 0 - 100.")
else:
    if score >= 70 and score <= 100:
        print("Grade is A")
    if score >= 60 and score <= 69:
        print("Grade is B")
    if score >= 55 and score <= 59:
        print("Grade is C")
    if score >= 50 and score <= 54:
        print("Grade is D")
    if score >= 45 and score <= 49:
        print("Grade is E")
    if score >= 35 and score <= 44:
        print("Grade is S")
    if score >= 0 and score <= 34:
        print("Grade is U")
