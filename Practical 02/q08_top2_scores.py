# Filename: q08_top2_scores.py
# Author: Chia Xiang Rong
# Date created: 29/1/13
# Date modified: 7/2/13
# Description: Prompts entry of number of students, their names and score,
# and displays name of top scorer and second highest scorer.

#Prompts entry of number of students
student_no = int(input("Enter total number of students: "))
i = 0
topScore = 0
secScore = 0
topName = str("name")
secName = str("name2")

while (i < student_no):
    name = str(input("Enter name of student: "))
    score = int(input("Enter score of " + format(name) + ": "))

    if score > topScore:
        secScore = topScore
        secName = topName
        topScore = score
        topName = name
    elif secScore < score < topScore:
        secScore = score
        secName = name
    else:
        pass

    i = i + 1

print("Top scorer is " + format(topName) + " with a score of " + format(topScore))
print("Second highest score is " + format(secName) + " with a score of " + format(secScore))

