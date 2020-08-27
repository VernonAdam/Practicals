"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit_conversion = fahrenheit_to_celsius(celsius)
            print("Result: {:.2f} F".format(fahrenheit_conversion))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit:"))
            celsius_conversion = celsius_to_fahrenheit(fahrenheit)
            print("Result: {:.2f} C".format(celsius_conversion))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def fahrenheit_to_celsius(celsius):
    fahrenheit_conversion = celsius * 9.0 / 5 + 32
    return fahrenheit_conversion


def celsius_to_fahrenheit(fahrenheit):
    celsius_conversion = (fahrenheit - 32) * 5 / 9
    return celsius_conversion


main()
