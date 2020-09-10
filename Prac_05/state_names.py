"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
state_names = {"QLD": "Queensland", "NSW": "New South Wales",
               "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria",
               "TAS": "Tasmania"}
state = input("Enter short state: ").upper()
while state != "":
    if state in state_names:
        print(state, "is", state_names[state])

    else:
        print("Invalid short state")

    state = input("Enter short state: ").upper()
