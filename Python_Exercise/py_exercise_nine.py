def student_score():
    scores = int(input("Enter scores: "))

    if 80 <= scores <= 100:
        result = "A"
    elif 79 >= scores >= 70:
        result = "B"
    elif 69 >= scores >= 60:
        result = "C"
    elif 59 >= scores >= 50:
        result = "D"
    elif 49 >= scores >= 40:
        result = "E"
    else:
        result = "F"

    score = f"your grade of ", {scores}, " earns you an", {result}, "in this course"
    print(score)


student_score()
