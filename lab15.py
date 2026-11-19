students = {
    "101": {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [85, 90, 78]
    },
    "102": {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [92, 88, 95]
    },
    "103": {
        "Name": "Karan",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [74, 80, 82]
    }
}

print("==================================================")
print("       STUDENT INFORMATION MANAGEMENT SYSTEM")
print("==================================================")

while True:
    print("")
    print("Select an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")
    print("")
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        print("")
        print("--- Enrolled Student Records ---")
        for roll, info in students.items():
            print(f"Roll No: {roll} | Name: {info['Name']:<8} | Branch: {info['Branch']} | Sem: {info['Semester']} | Marks: {info['Marks']}")
        print(f"Total Enrolled Students: {len(students)}")

    elif choice == "2":
        roll = input("Enter Roll Number to search: ")
        record = students.get(roll)
        print("")
        if record:
            print(f"[FOUND] Record for Roll No {roll}:")
            print(f"  Name     : {record['Name']}")
            print(f"  Branch   : {record['Branch']}")
            print(f"  Semester : {record['Semester']}")
            print(f"  Marks    : {record['Marks']}")
        else:
            print(f"[ERROR] No student found with Roll No {roll}.")

    elif choice == "3":
        print("")
        print("--- Register New Student ---")
        roll = input("Enter Roll Number: ")
        if roll in students:
            print(f"[ERROR] Roll Number {roll} already exists!")
        else:
            name = input("Enter Student Name: ")
            branch = input("Enter Branch (e.g. BCA AI): ")
            sem = input("Enter Semester: ")
            print("Enter marks obtained in 3 subjects:")
            m1 = int(input("  Subject 1: "))
            m2 = int(input("  Subject 2: "))
            m3 = int(input("  Subject 3: "))
            students[roll] = {
                "Name": name,
                "Branch": branch,
                "Semester": sem,
                "Marks": [m1, m2, m3]
            }
            print("")
            print(f"[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")

    elif choice == "4":
        roll = input("Enter Roll Number to update: ")
        if roll in students:
            print("Select field to update:")
            print("1. Branch")
            print("2. Semester")
            field = input("Enter choice (1-2): ")
            if field == "1":
                new_branch = input("Enter new Branch: ")
                students[roll]["Branch"] = new_branch
                print(f"[SUCCESS] Branch updated for Roll No {roll}.")
            elif field == "2":
                new_sem = input("Enter new Semester: ")
                students[roll]["Semester"] = new_sem
                print(f"[SUCCESS] Semester updated for Roll No {roll}.")
            else:
                print("[ERROR] Invalid field choice.")
        else:
            print(f"[ERROR] No student found with Roll No {roll}.")

    elif choice == "5":
        roll = input("Enter Roll Number for Academic Performance: ")
        record = students.get(roll)
        print("")
        if record:
            marks = record["Marks"]
            total = sum(marks)
            average = total / len(marks)
            if average >= 40:
                status = "PASS"
            else:
                status = "FAIL"
            print("================ ACADEMIC REPORT ================")
            print(f"Student Name : {record['Name']} (Roll: {roll})")
            print(f"Subject Marks: {marks}")
            print(f"Total Marks  : {total} / 300")
            print(f"Average Marks: {average:.2f}%")
            print(f"Final Result : {status}")
            print("=================================================")
        else:
            print(f"[ERROR] No student found with Roll No {roll}.")

    elif choice == "6":
        roll = input("Enter Roll Number to delete: ")
        removed = students.pop(roll, None)
        print("")
        if removed:
            print(f"[SUCCESS] Record for '{removed['Name']}' (Roll No: {roll}) deleted successfully.")
        else:
            print(f"[ERROR] No student found with Roll No {roll}.")

    elif choice == "7":
        print("")
        print("Thank you for using Student Information System. Goodbye!")
        break

    else:
        print("")
        print("[ERROR] Invalid choice! Please enter a number between 1 and 7.")
