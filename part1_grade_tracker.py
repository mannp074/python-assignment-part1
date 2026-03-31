# Name: Maan Lo
# ID: 2511765
# Assignment: GA3 (Part 1)

# =========================================
# Student Grade Tracker
# =========================================


# =========================
# Task 1 — Data Cleaning
# =========================

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

special_name = ""

print("\n--- Task 1 ---\n")

for stu in raw_students:
    # cleaning name (removing spaces + fixing case)
    clean_name = stu["name"].strip().title()

    # converting roll number to int
    roll_no = int(stu["roll"])

    # converting string marks into list
    student_marks = [int(x) for x in stu["marks_str"].split(", ")]

    # checking if name is valid (only alphabets)
    valid_flag = True
    for part in clean_name.split():
        if not part.isalpha():
            valid_flag = False

    if valid_flag:
        print("Valid name")
    else:
        print("Invalid name")

    print("-" * 30)
    print(f"Student : {clean_name}")
    print(f"Roll No : {roll_no}")
    print(f"Marks   : {student_marks}")
    print("-" * 30)

    if roll_no == 103:
        special_name = clean_name

print("\nRoll 103 student:")
print("Upper ->", special_name.upper())
print("Lower ->", special_name.lower())


# =========================
# Task 2 — Marks Analysis
# =========================

print("\n--- Task 2 ---\n")

subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
student_marks = [88, 72, 95, 60, 78]

# printing subject-wise grades
for sub, m in zip(subjects, student_marks):
    if m >= 90:
        g = "A+"
    elif m >= 80:
        g = "A"
    elif m >= 70:
        g = "B"
    elif m >= 60:
        g = "C"
    else:
        g = "F"

    print(sub, "->", m, "(", g, ")")

# basic calculations
total_marks = sum(student_marks)
avg_marks = round(total_marks / len(student_marks), 2)

print("\nTotal marks =", total_marks)
print("Average =", avg_marks)

# highest & lowest
max_m = max(student_marks)
min_m = min(student_marks)

print("Highest:", subjects[student_marks.index(max_m)], max_m)
print("Lowest:", subjects[student_marks.index(min_m)], min_m)

# taking extra subjects from user
count_new = 0

while True:
    s = input("\nEnter subject (or done): ")

    if s.lower() == "done":
        break

    m_input = input("Enter marks: ")

    if not m_input.isdigit():
        print("Please enter valid number")
        continue

    m_input = int(m_input)

    if m_input < 0 or m_input > 100:
        print("Marks should be 0–100")
        continue

    subjects.append(s)
    student_marks.append(m_input)
    count_new += 1

print("\nSubjects added =", count_new)
print("New average =", round(sum(student_marks) / len(student_marks), 2))


# =========================
# Task 3 — Class Summary
# =========================

print("\n--- Task 3 ---\n")

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("Name              | Avg | Result")
print("----------------------------------")

pass_cnt = 0
fail_cnt = 0

avg_list = []
top_name = ""
top_score = 0

for name, marks_list in class_data:
    avg_val = round(sum(marks_list) / len(marks_list), 2)

    if avg_val >= 60:
        result = "Pass"
        pass_cnt += 1
    else:
        result = "Fail"
        fail_cnt += 1

    print(f"{name:<18} | {avg_val:^5} | {result}")

    avg_list.append(avg_val)

    if avg_val > top_score:
        top_score = avg_val
        top_name = name

print("\nPass:", pass_cnt)
print("Fail:", fail_cnt)
print("Topper:", top_name, top_score)
print("Class avg:", round(sum(avg_list) / len(avg_list), 2))


# =========================
# Task 4 — String Work
# =========================

print("\n--- Task 4 ---\n")

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

clean_text = essay.strip()
print("Clean:\n", clean_text)

print("\nTitle:\n", clean_text.title())

count_py = clean_text.count("python")
print("\nCount of python:", count_py)

new_text = clean_text.replace("python", "Python 🐍")
print("\nReplaced:\n", new_text)

sent_list = clean_text.split(". ")
print("\nSentences:", sent_list)

print("\nNumbered:")
for i, line in enumerate(sent_list, 1):
    if not line.endswith("."):
        line += "."
    print(i, line)