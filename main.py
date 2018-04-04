import json

def loadSetupData():
    with open('gc_setup.json') as data_file:
        course = json.load(data_file)

    return course["course_setup"]

def loadStudentGrades():
    with open('gc_grades.json') as data_file:
        student_grades = json.load(data_file)

    grades = student_grades["mygrades"]
    return grades

def askForAssignmentMarks(grades,student_grades):
    current_grades = {"mygrades": {}}

    for key in grades:
        if student_grades[key] > -1:
            answer = raw_input ("Your grade from " + key + " is " + str(student_grades[key]) + ". Do you want to change your grade for " + key + "?" + " Please write yes or no.")
            if answer == "yes":
                student_answer = int(raw_input("What is your Current Grade for " + key + "? Please insert -1 if you don't have a grade yet."))
                if (student_answer >= 0 and student_answer <= 100) or (student_answer == -1):
                    current_grades["mygrades"][key] = student_answer
                else:
                    current_grades["mygrades"][key] = student_grades[key]
            elif answer == "no":
                current_grades["mygrades"][key] = student_grades[key]
        else:
            student_answer1 = raw_input("What is your Current Grade for " + key + "? Please insert -1 if you don't have a grade yet.")
            if (student_answer1 >= 0) and (student_answer1 <= 100) or (student_answer1 == -1):
                current_grades["mygrades"][key] = student_answer1
    return current_grades

def saveGrades(current_grades):
    print (json.dumps(current_grades))
    file = open("gc_grades.json", "w")
    file.write(json.dumps(current_grades))
    file.close()

def printCurrentGrade(grades,current_grades):
    curr_grade = 0
    for key in current_grades["mygrades"]:
        if current_grades["mygrades"][key] != -1:
            calc_grade = float(current_grades["mygrades"][key]) * grades[key] / 100
            curr_grade = curr_grade + calc_grade

    print float(curr_grade)
    return curr_grade

def printLetterGrade(grade, matrix):
    for i in range(len(matrix)):
        if matrix[i]["min"] <= grade and matrix[i]["max"] >= grade:
            print matrix[i]["mark"]

def main():
    course = loadSetupData()
    grades = course["grade_breakdown"]
    conv_matrix = course["conv_matrix"]
    student_grades = loadStudentGrades()
    current_grades = askForAssignmentMarks(grades, student_grades)
    saveGrades(current_grades)
    curr_grade = printCurrentGrade(grades, current_grades)
    printLetterGrade(curr_grade, conv_matrix)

main()