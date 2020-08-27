"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
The value error will occur if user inputs a string instead of a int
2. When will a ZeroDivisionError occur?
If either the numerator or the denominator are zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
You can
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
