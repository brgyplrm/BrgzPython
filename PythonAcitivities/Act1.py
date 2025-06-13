def fibonacci_up_to_number(num):

    # initialize the first two terms sigma
    a, b = 1, 1

    # Create a list to store the Fibonacci sequence
    fibtup = [a]

    # generate the Fibonacci sequence until the last term is <= max_number
    while b <= num:
        fibtup.append(b)
        a, b = b, a + b
    # Convert the list to a tuple
    return tuple(fibtup)

#user input for the postive or negative
user_input = int(input("Enter a number: "))

if user_input < 0:
        print("Invalid")
else:
        fibtup = fibonacci_up_to_number(user_input)
        print(fibtup)


