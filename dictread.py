# import csv

# with open ("people.csv", "w") as file:
#     b = csv.DictWriter(file)

    # for i in b:
    #     #print(i)
    #     print(f'{i['name']} is{i[' age']} old')

import csv

header = ["name", "maths", "english", "science", "agric"]
students = []


def get_name():
    while True:
        name = input("Enter student name: ").strip()

        if not name:
            print("Name cannot be empty. Try again.")
            continue
        return name

def get_score(subject):
    while True:
        try:
            score = int(input(f"Enter {subject} score (0-30): "))

            if score < 0 or score > 30:
                print("Score must be between 0 and 30.")
                continue

            return score

        except ValueError:
            print("Invalid input. Please enter an integer.")


while True:

    name = get_name()

    student = {
        "name": name,
        "maths": get_score("Maths"),
        "english": get_score("English"),
        "science": get_score("Science"),
        "agric": get_score("Agric")
    }

    students.append(student)

    print(f"\n{name} successfully registered!")

    while True:
        choice = input(
            "\nDo you want to add another student? (y/n): "
        ).strip().lower()

        if choice == "y":
            break

        elif choice == "n":
            print("\nRegistration completed!")
            break

        else:
            print("Invalid choice. Enter y or n.")

    if choice == "n":
        break


with open("score_sheet.csv", "w", newline="") as file:

    writer = csv.DictWriter(file, fieldnames=header)

    writer.writeheader()
    writer.writerows(students)

print("\nAll student records saved successfully!")

with open("score_sheet.csv", "r") as file:
    reader = csv.DictReader(file)

    for student in reader:
        name = student["name"]

        maths = int(student["maths"])
        english = int(student["english"])
        science = int(student["science"])
        agric = int(student["agric"])

with open("score_sheet.csv", "r", newline="") as file:

    reader = csv.DictReader(file)

    for student in reader:

        name = student["name"]
        maths = int(student["maths"])
        english = int(student["english"])
        science = int(student["science"])
        agric = int(student["agric"])

        maths_bonus = 5 if maths <= 25 else 30 - maths
        english_bonus = 5 if english <= 25 else 30 - english
        science_bonus = 5 if science <= 25 else 30 - science
        agric_bonus = 5 if agric <= 25 else 30 - agric

        maths_final = maths + maths_bonus
        english_final = english + english_bonus
        science_final = science + science_bonus
        agric_final = agric + agric_bonus

        original_total = maths + english + science + agric

        total_bonus = (
            maths_bonus + english_bonus +
            science_bonus + agric_bonus
        )

        final_total = original_total + total_bonus

        print("\n" + "=" * 50)
        print("             STUDENT SCORE REPORT")
        print("=" * 50)

        print(f"Student Name: {name}")

        print("-" * 50)
        print(f"{'Subject':<12}{'Original':<12}{'Bonus':<10}{'Final':<10}")
        print("-" * 50)

        print(f"{'Maths':<12}{maths:<12}{maths_bonus:<10}{maths_final:<10}")
        print(f"{'English':<12}{english:<12}{english_bonus:<10}{english_final:<10}")
        print(f"{'Science':<12}{science:<12}{science_bonus:<10}{science_final:<10}")
        print(f"{'Agric':<12}{agric:<12}{agric_bonus:<10}{agric_final:<10}")

        print("-" * 50)
        print(f"Original Total: {original_total}/120")
        print(f"Total Bonus:    {total_bonus}")
        print(f"FINAL TOTAL:    {final_total}/120")
        print("=" * 50)