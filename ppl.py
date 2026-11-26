import os

def load_records():
    records = []

    try:
        with open("ppl.txt", "r") as file:
            for line in file:
                line = line.strip()
                fields = line.split("|")
                if len(fields) != 4:
                    print("warning: Malformed record skipped.")
                    continue
                name = fields[0].strip()
                age = fields[1].strip()
                address = fields[2].strip()
                occupation = fields[3].strip()

                try:
                    age = int(age)
                except ValueError:
                    print("Warning: Invalid age record skipped.")
                    continue

                if not name or not address or not occupation or age <= 0:
                    print("Warning: Invalid record skipped")
                    continue
                person = {
                    "name": name,
                    "age": age,
                    "address": address,
                    "occupation": occupation                
                }

                records.append(person)
    except FileNotFoundError:
        print("no records file found.")
    return records

def save_records(records):
    with open ("ppl.txt", "w") as file:
        for person in records:
            line = (
                f"{person['name']}|"
                f"{person['age']}|"
                f"{person['address']}|"
                f"{person['occupation']}\n"
            )   
            file.write(line)

def get_name():
    while True:
        name = input("Enter name: ").strip()

        if not name:
            print("cannot be empty.")
            continue
        if "|" in name:
            print("Name cannot contain |.")
            continue
        return name

def get_age():
    while True:
        age = input("Enter age: ").strip()

        if not age:
            print("age cannot be empty.")
        try:
            age = int(age)
        except ValueError:
            print("Age must be a whole number")
            continue
        if age <= 0:
            print("Age cannot be negative")
            continue
        return age

def get_address():
    while True:
        address = input("Enter your address: ").strip()

        if not address:
            print("address cannot be empty")
            continue
        if "|" in address:
            print("address cannot contain |.")
            continue
        return address

def get_occupation():
    while True:
        occupation = input("Enter Occupation: ")

        if not occupation:
            print("Occcupation cannot be empty.")
            continue
        if "|" in occupation:
            print("Occupation cannot contain |.")
            continue
        return occupation

def show_all():
    records = load_records()

    if not records:
        print("No records found")
        return
    for number, person in enumerate(records, start = 1):
        print(f"\n{number}. Name: {person['name']}")
        print(f"    Age: {person['age']}")
        print(f"    Address: {person['address']}")
        print(f"    Occupation: {person['occupation']}")

def add_person():
    records = load_records()
    name = get_name()

    for person in records:
        if person["name"].lower() == name.lower():
            print("A person with this name alresdy exist.")
            return
    age = get_age()
    address = get_address()
    occupation = get_occupation()

    person = {
        "name": name,
        "age": age,
        "address": address,
        "occupation": occupation
    }
    records.append(person)
    save_records(records)
    print(f"{person['name']} printed succesfully")

def search_person():
    records = load_records()
    search_text = input("Enter name to search: ").strip().lower()
    if not search_text:
        print("Search cannot be empty.")
        return
    found = False
    for person in records:
        if search_text in person["name"].lower():
            print(f"\nName: {person['name']}")
            print(f"Age: {person['age']}")
            print(f"Address: {person['address']}")
            print(f"Occupation: {person['occupation']}")
            found = True
    if not found:
        print("No matching person found.")

def update_person():
    records = load_records()
    if not records:
        print("No record to update.")
        return
    show_all()

    try:
        choice = int(input("Enter the record number to update: "))
    except ValueError:
        print("Please enter a valid number")
        return

    if choice < 1 or choice > len(records):
        print("Invalid record number.")
        return

    person = records[choice - 1]

    name = input(f" New name ({person['name']}): ").strip()
    if name:
        if "|" in name:
            print("name cannot contain |.")
            return
        if any(
            p["name"].lower() == name.lower()
            for i, p in enumerate(records)
            if i != choice - 1
        ):
            print("That name already exists.")
            return
        person["name"] = name

    age = input(f"New age ({person['age']}): ").strip()
    if age:
        try:
            age = int(age)
            if age < 0:
                print("Age cannot be negative")
                return
            person["age"] = age
        except ValueError:
            print("Age must be a whole number.")
            return

    address = input(f"New address ({person['address']}): ").strip()
    if address:
        if "|" in address:
            print("Adress cannot contain |.")
            return
        person["address"] = address

    occupation = input(f"New occupation ({person['occupation']}): ").strip()
    if occupation:
        if "|" in occupation:
            print("Occupation cannot contain |.")
            return
        person["occupation"] = occupation

    save_records(records)
    print("Record updated successfully!")

def delete_person():
    records = load_records()
    if not records:
        print("No records to delete.")
        return
    show_all()

    try:
        choice = int(input("\nEnter the record number to delete: "))
    except ValueError:
        print("please enter a valid number.")
        return

    if choice < 1 or choice > len(records):
        print("Invalid record number")
        return
    person = records[choice - 1]

    print(f"You selected: {person['name']}")
    confirm = input("Are you sure? [y/N]: ").strip().lower()
    if confirm == "y":
        records.pop(choice - 1)
        save_records(records)
        print("Record deleted successfully!")
    else:
        print("Deletion cancelled.")

def delete_file():
    confirm = input("Are you sure you want to delete All records? [y/N]:").strip().lower()
    if confirm != "y":
        print("Deletion cancelled.")
        return

    try:
        os.remove("people.txt")
        print("Records file deleted successfully!")
    except FileNotFoundError:
        print("The records file does not exist.")

def main():
    while True:
        print("\n===== PEOPLE MANAGER =====")
        print("1. Show all records")
        print("2. Add a person")
        print("3. Search for a person")
        print("4. Update a person")
        print("5. Delete a person")
        print("6. Delete entire file")
        print("7. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_all()
        elif choice == "2":
            add_person()
        elif choice == "3":
            search_person()
        elif choice == "4":
            update_person()
        elif choice == "5":
            delete_person()
        elif choice == "6":
            delete_file()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-7.")
if __name__ == "__main__":
    main()