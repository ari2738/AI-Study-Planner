from datetime import datetime

print("===== AI STUDY PLANNER =====")

# Get user input
subjects = []
n = int(input("Enter number of subjects: "))

for i in range(n):
    sub = input(f"Enter subject {i+1} name: ")
    subjects.append(sub)

exam_date_input = input("Enter exam date (YYYY-MM-DD): ")
daily_hours = float(input("Enter how many hours you can study per day: "))

# Convert exam date
exam_date = datetime.strptime(exam_date_input, "%Y-%m-%d")
today = datetime.today()

days_left = (exam_date - today).days

if days_left <= 0:
    print("Exam date already passed or today!")
else:
    print("\nDays left for exam:", days_left)

    total_hours = days_left * daily_hours
    hours_per_subject = total_hours / len(subjects)

    print("\n===== STUDY PLAN =====")
    print("Total Study Hours Available:", total_hours)
    print("Hours per Subject:", round(hours_per_subject, 2))

    print("\nDaily Study Distribution:")
    daily_subject_time = daily_hours / len(subjects)

    for sub in subjects:
        print(f"{sub} -> {round(daily_subject_time,2)} hours per day")

print("\nStay consistent 💪 You can do it!")
