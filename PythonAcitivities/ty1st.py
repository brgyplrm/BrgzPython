def russian_multiplication(a, b):
    result = 0
    steps = []
    sum_second_values = 0

    while a > 0:
        steps.append((a, b))
        if a % 2 != 0:
            result += b
            sum_second_values += b
        a //= 2
        b *= 2
    return result, steps, sum_second_values

def GreatesCommonDivisor(a, b, steps=None):
    if steps is None:
        steps = []  # Initialize steps list only on the first call

    steps.append(f"gcd({a}, {b})")  # Record the current step

    if a == 0:
        return b, steps  # Base case: return GCD and the steps

    # Recursive case: call the function with (b % a, a)
    return GreatesCommonDivisor(b % a, a, steps)

firstNum = int(input("Enter a first number: "))
secondNum = int(input("Enter a second number: "))

if firstNum <= 0 or secondNum <= 0:
    print("Error! Positive integer only")
else:
    product, steps_russian, sum_second_values = russian_multiplication(firstNum, secondNum)

    gcd, steps_gcd = GreatesCommonDivisor(firstNum, secondNum)

    print("\nOutput")
    for a, b in steps_russian:
        print(f"{a:4}  {b:4}")

    print(f"\nProduct: {product}")
    if firstNum % 2 != 0:
        print(f"Sum of second number values: {sum_second_values}\n\n")

    for step in steps_gcd:
        print(step)

    print(f"gcd({gcd})")