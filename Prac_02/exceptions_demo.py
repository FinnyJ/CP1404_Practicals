"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur when string or any non-numeric value is entered in any of the inputs.
2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur when a "0" is entered into the denominator input as its not possible to devide a number by 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero! Try Again")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
#except ZeroDivisionError:
#   print("Cannot divide by zero!")
print("Finished.")