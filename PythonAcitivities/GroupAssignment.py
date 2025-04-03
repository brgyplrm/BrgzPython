from GroupAssClass import *

subCount = 0


def StudentInput():
    global subCount

    while True:
        with open("StudentRec.txt", "r") as stdno:
            StudNo = input("\nEnter Student Number: ")
            stdno_content = stdno.read()

            if StudNo not in stdno_content:
                if not StudNo:
                    print("Empty Number")
                    continue
                elif StudNo.isdigit():
                    StudNo = int(StudNo)
                else:
                    print("Invalid Input")
                    continue
            else:
                print(f"{StudNo} is already in the list")
                continue

        with open("StudentRec.txt", "r") as stdna:
            StudNa = input("Enter Student Name: ").capitalize()
            stdna_content = stdna.read()

            if StudNa not in stdna_content:
                if not StudNa:
                    print("Empty Name")
                    continue
                else:
                    StudNa = str(StudNa)
            else:
                print(f"{StudNa} is already in the records")
                continue

        while True:
            try:
                maxSub = int(input("Enter the number of subjects: "))
                print("\n")
                if maxSub <= 0:
                    print("Invalid.")
                    continue
                break
            except ValueError:
                print("Invalid input.")
                continue

        # Append Student record first
        StdRec = Student(StudNo, StudNa, maxSub)
        StdRec.AppendStudent()

        subject_count = 0
        for i in range(maxSub):
            with open("StudentRec.txt", "r") as sbCode:
                SubCode = input("Enter Subject Code: ").upper()
                if not SubCode:
                    print("Empty Code")
                    continue

            SubDesc = input("Enter Subject Description: ")
            if not SubDesc:
                print("Empty Description")
                continue

            NoofUnits = input("Enter Number of Units: ")
            if not NoofUnits:
                print("Empty Units")
                continue
            try:
                NoofUnits = int(NoofUnits)
            except ValueError:
                print("Invalid Input")
                continue

            MidGrade = input("Enter Midterm Grade: ")
            if not MidGrade:
                print("Empty Grade")
                continue
            try:
                MidGrade = float(MidGrade)
            except ValueError:
                print("Invalid Input")
                continue

            FinalGrade = input("Enter Final Grade: ")
            if not FinalGrade:
                print("Empty Grade")
                continue
            try:
                FinalGrade = float(FinalGrade)
            except ValueError:
                print("Invalid Input")
                continue
            AverageGrade = (MidGrade + FinalGrade) / 2

            if AverageGrade <= 3.2:
                Remarks = "Passed"
            else:
                Remarks = "Failed"

            subject_count += 1
            subCount = subject_count

            print("\n")

            SubRec = Subject(SubCode, SubDesc, NoofUnits, MidGrade, FinalGrade, AverageGrade, Remarks)
            SubRec.AppendSubject()

            if subject_count >= maxSub:
                print("\nMaximum subject count reached for this student.\n")
                break

        inputStudent = input("Input Student again? Yes or No: ").capitalize()
        if inputStudent == "No":
            print("Student Records Input")
            print("----------------------")
            print("  [A] Add Students    ")
            print("  [B] Edit Students   ")
            print("  [C] Delete Students ")
            print("  [D] View Students   ")
            print("  [E] Exit Subject    ")
            print("----------------------")
            return
        else:
            print(f"Input Successful for Student {StudNo}")
            print("\n")


def StudentEdit():
    studSearchList = []
    sublist = []

    with open("StudentRec.txt", "r") as studSearch1:
        studSearchLine = studSearch1.readlines()

    with open("StudentRec.txt", "r") as studSearch2:
        studSearchLen = len(studSearch2.readlines())

    for i in range(0, studSearchLen):
        line = studSearchLine[i].strip().split(" ")
        studSearchList.append(line)

    while True:
        SearchStud = input("Enter Student Num: ")
        found = False
        sublist = []

        for i in range(0, studSearchLen):
            if SearchStud == studSearchList[i][0]:
                found = True
                count = int(studSearchList[i][2])
                start = i + 1
                end = start + count

                for j in range(start, end):
                    sublist.append(studSearchList[j])

                print(f"\nStudent Number: {studSearchList[i][0]}")
                print(f"Student Name: {studSearchList[i][1]}\n")

                inputNewName = input("New Name: ")

                inputNewName = inputNewName.capitalize()
                studSearchList[i][1] = inputNewName

                print("\nUpdated Student Record")
                print("Student Number:", studSearchList[i][0])
                print("Student Name:", studSearchList[i][1], "\n")

        if found:
            while True:
                for i in range(0, len(sublist)):
                    print(f"Subject Code: {sublist[i][0]}")

                valid_sub_code = False
                while not valid_sub_code:
                    SubCode = input("\nEnter Subject Code to change: ").upper()
                    for i in range(0, len(sublist)):
                        if sublist[i][0] == SubCode:
                            valid_sub_code = True
                            NewSubCode = input("\nEnter New Subject Code: ").upper()
                            sublist[i][0] = NewSubCode

                            try:
                                NewMidGrade = float(input("Enter New Midterm Grade: "))
                                sublist[i][3] = NewMidGrade
                            except ValueError:
                                print("Invalid Input. Please enter a valid midterm grade.")
                                continue

                            try:
                                NewFinalGrade = float(input("Enter New Final Grade: "))
                                sublist[i][4] = NewFinalGrade
                            except ValueError:
                                print("Invalid Input. Please enter a valid final grade.")
                                continue

                            NewAve = (NewMidGrade + NewFinalGrade) / 2
                            sublist[i][5] = NewAve

                            if NewAve <= 3.2:
                                remarks = "Passed"
                                sublist[i][6] = remarks
                            else:
                                remarks = "Failed"
                                sublist[i][6] = remarks
                            break

                    if not valid_sub_code:
                        print("Subject Code not found. Please try again.")

                inputSubCodeAgain = input("Input another Subject Code? Yes or No: ").capitalize()
                if inputSubCodeAgain != "Yes":
                    break

            print("\nUpdated Subject Record")
            y = 0
            x = 0

            with open("StudentRec.txt", "w") as studentUpdate:
                while x < len(studSearchList):
                    for i in range(0, 3):
                        if i == 2:
                            studUpdate = f"{studSearchList[x][i]}\n"
                            studentUpdate.write(studUpdate)

                            count = int(studSearchList[x][i])
                            x += 1
                            break
                        else:
                            studUpdate = f"{studSearchList[x][i]} "
                            studentUpdate.write(studUpdate)

                    y = 0
                    while y < count:
                        for j in range(0, 7):
                            if j == 6:
                                studUpdate = f"{studSearchList[x][j]}\n"
                                studentUpdate.write(studUpdate)
                                x += 1
                                break
                            else:
                                studUpdate = f"{studSearchList[x][j]} "
                                studentUpdate.write(studUpdate)
                        y += 1
        else:
            print("Student Number not found. Please try again.")

        editAgain = input("Edit another student? Yes or No: ").capitalize()
        if editAgain != "Yes":
            print("\nStudent Records Input")
            print("----------------------")
            print("  [A] Add Students    ")
            print("  [B] Edit Students   ")
            print("  [C] Delete Students ")
            print("  [D] View Students   ")
            print("  [E] Exit Subject    ")
            print("----------------------")
            return

def StudentDelete():
    sublist = []
    studSearchList = []

    with open("StudentRec.txt", "r") as studSearch1:
        studSearchLine = studSearch1.readlines()

    with open("StudentRec.txt", "r") as studSearch2:
        studSearchLen = len(studSearch2.readlines())

    for i in range(0, studSearchLen):
        line = studSearchLine[i].strip().split(" ")
        studSearchList.append(line)

    while True:
        SearchStud = input("Enter Student Number to delete: ")
        found = False
        updatedList = []

        for i in range(0, studSearchLen):
            if SearchStud == studSearchList[i][0]:
                found = True
                count = int(studSearchList[i][2])
                start = i + 1 + count

                studSearchList = studSearchList[:i] + studSearchList[start:]
                break

        if found:
            with open("StudentRec.txt", "w") as studentUpdate:
                for record in studSearchList:
                    studentUpdate.write(" ".join(map(str, record)) + "\n")
            print(f"Student with Student Number {SearchStud} has been deleted successfully.")
        else:
            print("Student Number not found. Please try again.")
            continue

        deleteAgain = input("Delete another student? Yes or No: ").capitalize()
        if deleteAgain != "Yes":
            print("\nStudent Records Input")
            print("----------------------")
            print("  [A] Add Students    ")
            print("  [B] Edit Students   ")
            print("  [C] Delete Students ")
            print("  [D] View Students   ")
            print("  [E] Exit Subject    ")
            print("----------------------")
            return

def StudentView():
    try:
        with open("StudentRec.txt", "r") as file:
            records = file.read()
            if records.strip():
                print("\nStudent Records:\n")
                print(records)
            else:
                print("No records found.\n")
    except FileNotFoundError:
        print("StudentRec.txt file not found.")

    print("Student Records Input")
    print("----------------------")
    print("  [A] Add Students    ")
    print("  [B] Edit Students   ")
    print("  [C] Delete Students ")
    print("  [D] View Students   ")
    print("  [E] Exit Subject    ")
    print("----------------------")
    return

def Studentexit():
    print("Exiting Subject")
    exit()

print("Student Records Input")
print("----------------------")
print("  [A] Add Students    ")
print("  [B] Edit Students   ")
print("  [C] Delete Students ")
print("  [D] View Students   ")
print("  [E] Exit Subject    ")
print("----------------------")

while True:
    userInput = input("Enter your choice: ").capitalize()

    if userInput == 'A':
        StudentInput()
    elif userInput == 'B':
        StudentEdit()
    elif userInput == 'C':
        StudentDelete()
    elif userInput == 'D':
        StudentView()
    elif userInput == 'E':
        Studentexit()
    else:
        print("Invalid Input")
        continue