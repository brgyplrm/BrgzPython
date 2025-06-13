def Winner(person, index, direction, killed):
    if len(person) == 1:
        print("Players killed:", killed)
        print("The winner is:", person[0])
        return

    Killed(person, k, index, direction, killed)

def Killed(persons, k, index, direction, killed):
    if direction == "Clockwise":
        index = (index + k) % len(persons)
    elif direction == "Counterclockwise":
        index = (index - k) % len(persons)
    else:
        print("Invalid Direction")
        return

    killed.append(persons.pop(index))

    Winner(persons, index, direction, killed)

n = int(input("Number of Players: "))
if n < 8 or n > 20:
    print("Invalid input")
    exit()

k = int(input("Number of skips: "))
if k <= 0:
    print("Invalid input")
    exit()

start = int(input("Starting Point: "))
if start < 1 or start > n:
    print("Invalid input")
    exit()

direction = input("Direction: ").capitalize()
if direction != "Clockwise" and direction != "Counterclockwise":
    print("Invalid Direction")
    exit()

index = start - 1  # Fix: Convert starting point to 0-based index

person = []
for i in range(1, n + 1):
    person.append(i)

killed = []
Killed(person, k, index, direction, killed)