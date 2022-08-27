Quizgrades = open("quiz1grades.txt","r")
Quizgrades_analysis = open("quiz1grades_analysis.txt","w+")

Scores = {"0-20": 0, "20-40": 0, "40-60": 0, "60-80": 0, "80-100": 0}
for x in Quizgrades:
    if int(x) > 0 and int(x) <= 20:
        Scores["0-20"] += 1
    if int(x) > 20 and int(x) <= 40:
        Scores["20-40"] += 1
    if int(x) > 40 and int(x) <= 60:
        Scores["40-60"] += 1
    if int(x) > 60 and int(x) <= 80:
        Scores["60-80"] += 1
    if int(x) > 80 and int(x) <= 100:
        Scores["80-100"] += 1

Quizgrades_analysis.write("The number of students who scored between 0 and 20 is:")
Quizgrades_analysis.write(str(Scores["0-20"]))
Quizgrades_analysis.write("\n")
Quizgrades_analysis.write("The number of students who scored between 20 and 40 is:")
Quizgrades_analysis.write(str(Scores["20-40"]))
Quizgrades_analysis.write("\n")
Quizgrades_analysis.write("The number of students who scored between 40 and 60 is:")
Quizgrades_analysis.write(str(Scores["40-60"]))
Quizgrades_analysis.write("\n")
Quizgrades_analysis.write("The number of students who scored between 60 and 80 is:")
Quizgrades_analysis.write(str(Scores["60-80"]))
Quizgrades_analysis.write("\n")
Quizgrades_analysis.write("The number of students who scored between 80 and 100 is:")
Quizgrades_analysis.write(str(Scores["80-100"]))