student_data = {
    "Aastha": {
        "Python": 99,
        "Math": 98,
        "Database": 95
    },
    "Rohan": {
        "Python": 78,
        "Math": 82,
        "Database": 80
    },
    "Priya": {
        "Python": 95,
        "Math": 91,
        "Database": 89
    },
    "Rahul": {
        "Python": 65,
        "Math": 70,
        "Database": 72
    },
    "Neha": {
        "Python": 90,
        "Math": 91,
        "Database": 80
    }
}

top_student = ""
highest_avg = 0

for name , subject in student_data.items():
        # print(f"{name} {subject}")
        score = subject.values()
        total_score = sum(score)
        avg = total_score / len(score)

        if avg >= 90:
                grade = 'A'
        elif avg >=80:
                grade = 'B' 
        elif avg >=70:
                grade = 'C'
        else:
                grade = 'D'
        print(f"{name:<12}- average: {avg:.2f}% | grade: {grade}")

        if avg > highest_avg:
                highest_avg = avg
                top_student = name 

print(f"Class Topper is {top_student} with {highest_avg:.2f}%!")